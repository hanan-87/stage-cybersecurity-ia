import requests
import time

def start_agent():
    print("[*] L'Agent Autonome de Sécurité en écoute...")
    
    # Simulation de différents scénarios (BENIGN et ATTAQUES)
    fake_traffic_stream = [
        {"ip": "192.168.1.50", "port": 443, "len": 54, "dur": 0.1, "type": "BENIGN"},
        {"ip": "10.0.0.99", "port": 80, "len": 9999, "dur": 0.001, "type": "DDoS"}, 
        {"ip": "172.16.0.5", "port": 22, "len": 450, "dur": 2.1, "type": "Brute Force"},
        {"ip": "192.168.1.200", "port": 8080, "len": 0, "dur": 0.0, "type": "PortScan"}
    ]
    
    for traffic in fake_traffic_stream:
        time.sleep(3)
        print(f"\n[*] Analyse du trafic depuis {traffic['ip']}...")
        
        payload = {
            "ip": traffic["ip"],
            "destination_port": traffic["port"],
            "packet_length": traffic["len"],
            "duration": traffic["dur"],
            "attack_type": traffic["type"]
        }
        
        try:
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)
            res = response.json()["result"]
            print(f"[+] Résultat : {res}")
            
            if res != "BENIGN":
                print(f"[-] 🔥 🚨 [ALERTE] Blocage de l'IP {traffic['ip']} (Type: {res})")
            else:
                print(f"[+] [OK] Trafic autorisé.")
        except Exception as e:
            print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    start_agent()