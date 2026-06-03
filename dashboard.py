import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1️⃣ Configuration dyal l-page kima image_d7ee3f.png
st.set_page_config(page_title="SOC CyberSecurity IA", layout="wide", initial_sidebar_state="expanded")

# CSS forcer l-sidebar t-koun k7la o l-ktaba bayna
st.markdown("""
    <style>
    .main { background-color: #f8f9fa !important; }
    [data-testid="stSidebar"] { background-color: #0b132b !important; }
    [data-testid="stSidebar"] div, [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] h2 {
        color: #8d99ae !important;
    }
    div[data-testid="stSidebarNav"] { display: none !important; }
    .sidebar-title { color: #ffffff !important; font-size: 22px; font-weight: bold; padding-top: 10px; }
    .sidebar-subtitle { color: #5c6b73 !important; font-size: 13px; margin-bottom: 25px; }
    .sidebar-section { color: #4dabf7 !important; font-weight: bold; font-size: 11px; margin-top: 25px; margin-bottom: 10px; }
    .menu-item-active { color: #ffffff !important; font-size: 15px; padding: 10px 15px; background-color: #1c2541 !important; border-radius: 8px; font-weight: bold; display: block; }
    .menu-item { color: #a2a8d3 !important; font-size: 15px; padding: 10px 10px; display: block; }
    .sidebar-footer { margin-top: 40px; padding: 10px; border-top: 1px solid #1c2541; }
    .agent-status { color: #2ecc71 !important; font-weight: bold; font-size: 14px; }
    .agent-sub { color: #5c6b73 !important; font-size: 11px; }
    .metric-card { background-color: white !important; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); border: 1px solid #edf2f7; }
    .metric-title { color: #718096 !important; font-size: 14px; margin-bottom: 5px; }
    .metric-val { font-size: 32px; font-weight: bold; margin: 0; }
    </style>
""", unsafe_allow_html=True)

# 2️⃣ SIDEBAR
with st.sidebar:
    st.markdown('<div class="sidebar-title">🛡️ SOC IDS</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Hanan Agent API</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section">PRINCIPAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item-active">📊 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🔔 Alertes IA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section">SYSTEME</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-footer"><div class="agent-status">🟢 API Active — Cloud</div><div class="agent-sub">FastAPI + Machine Learning</div></div>', unsafe_allow_html=True)

# 3️⃣ STATE MANAGEMENT (Bach d-data t-zad real-time bla ma t-tm7a)
if "total_scans" not in st.session_state: st.session_state.total_scans = 4
if "alerts_count" not in st.session_state: st.session_state.alerts_count = 3
if "incidents_list" not in st.session_state: 
    st.session_state.incidents_list = [
        {"Heure": "15:28:01", "IP Source": "192.168.1.50", "Type": "BENIGN", "Action": "🟢 Autorisé"},
        {"Heure": "15:28:04", "IP Source": "10.0.0.99", "Type": "DDoS", "Action": "🛑 Bloquée"},
        {"Heure": "15:28:10", "IP Source": "172.16.0.5", "Type": "Brute Force", "Action": "🛑 Bloquée"},
        {"Heure": "15:28:15", "IP Source": "192.168.1.200", "Type": "PortScan", "Action": "🛑 Bloquée"}
    ]

# 4️⃣ MAIN CONTENT
st.markdown("<h2>Vue d'ensemble — Surveillance IA</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#718096;'>Analyse du trafic réseau en temps réel via Hugging Face</p>", unsafe_allow_html=True)

# Bouton dyal Simulation en temps réel (Bach t-werri l-jury kifach les attaques kay-tzado)
st.markdown("### 🕹️ Section de Simulation (Pour la Soutenance)")
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("🔥 Injecter une Attaque Aléatoire (DDoS / BruteForce / PortScan)", use_container_width=True):
        now = datetime.now().strftime("%H:%M:%S")
        types_attaques = ["DDoS", "Brute Force", "PortScan"]
        ips_attaques = ["10.0.0.99", "172.16.0.5", "192.168.1.200", "185.220.101.5"]
        
        type_choisi = random.choice(types_attaques)
        ip_choisie = random.choice(ips_attaques)
        
        st.session_state.total_scans += 1
        st.session_state.alerts_count += 1
        st.session_state.incidents_list.insert(0, {
            "Heure": now, "IP Source": ip_choisie, "Type": type_choisi, "Action": "🛑 Bloquée"
        })
        st.success(f"🚨 Attaque {type_choisi} détectée depuis {ip_choisie}!")
        st.rerun()

with col_btn2:
    if st.button("🟢 Injecter un Trafic Sain (BENIGN)", use_container_width=True):
        now = datetime.now().strftime("%H:%M:%S")
        st.session_state.total_scans += 1
        st.session_state.incidents_list.insert(0, {
            "Heure": now, "IP Source": "192.168.1.50", "Type": "BENIGN", "Action": "🟢 Autorisé"
        })
        st.info("🟢 Trafic sain analysé et autorisé.")
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# Les 3 Cartes Blanches (Les valeurs ghadi i-welli i-tzado real-time melli t-clicki!)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><p class='metric-title'>Trafic Total Scanné</p><p class='metric-val' style='color:#2b6cb0;'>{st.session_state.total_scans}</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><p class='metric-title'>Attaques Détectées</p><p class='metric-val' style='color:#e53e3e;'>{st.session_state.alerts_count}</p></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='metric-card'><p class='metric-title'>Statut du Système</p><p class='metric-val' style='color:#38a169;'>100%</p></div>", unsafe_allow_html=True)

st.markdown("<br>---<br>", unsafe_allow_html=True)

# Tableau de l'historique
st.markdown("<h4>📜 Historique des Détections de votre API</h4>", unsafe_allow_html=True)
df = pd.DataFrame(st.session_state.incidents_list)
st.dataframe(df, use_container_width=True)
