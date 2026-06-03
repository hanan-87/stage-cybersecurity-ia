from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import sqlite3
from datetime import datetime

app = FastAPI()

# 1. Chargement des modèles (Les 32 features)
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
features_cols = joblib.load('features.pkl')

def init_db():
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, 
                       ip_source TEXT, prediction TEXT, details TEXT)''')
    conn.commit()
    conn.close()

init_db()

class PacketData(BaseModel):
    ip: str
    destination_port: float
    packet_length: float
    duration: float
    attack_type: str = "BENIGN"  # Bach n-simuliw attacks f l-soutenance

@app.post("/predict")
def predict_traffic(data: PacketData):
    # Si l'agent force une attaque pour la démo
    if data.attack_type != "BENIGN":
        prediction_str = data.attack_type
    else:
        # Utilisation de l'IA avec les 32 features
        input_dict = {col: 0 for col in features_cols} # Initialiser tout à 0
        input_dict['Destination Port'] = data.destination_port
        input_dict['Total Length of Fwd Packets'] = data.packet_length
        input_dict['Flow Duration'] = data.duration
        
        input_df = pd.DataFrame([input_dict])
        input_df = input_df.reindex(columns=features_cols, fill_value=0)
        scaled_data = scaler.transform(input_df)
        pred = model.predict(scaled_data)[0]
        prediction_str = "BENIGN" if str(pred) == "0" else f"ATTACK_{pred}"

    # Sauvegarde dans SQLite
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (timestamp, ip_source, prediction, details) VALUES (?, ?, ?, ?)",
                   (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data.ip, prediction_str, f"Port: {data.destination_port}"))
    conn.commit()
    conn.close()
    
    return {"result": prediction_str}