import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Cyber-IA Dashboard", layout="wide")

st.title("🛡️ Dashboard de Sécurité IA - Stage Hanane")
st.write("Surveillance en temps réel des flux réseau et décisions de l'IA")

# Connexion à la base de données
conn = sqlite3.connect('incidents.db')
df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC", conn)
conn.close()

# Statistiques simples
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Flux Analysés", len(df))
with col2:
    attacks = len(df[df['prediction'] != 'BENIGN'])
    st.metric("Alertes Détectées", attacks)

# Affichage du tableau
st.subheader("📋 Historique des Incidents")
st.dataframe(df, use_container_width=True)

# Graphique simple (Optionnel)
if not df.empty:
    st.subheader("📈 Répartition des prédictions")
    st.bar_chart(df['prediction'].value_counts())