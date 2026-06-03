import streamlit as st
import pandas as pd

# 1️⃣ Configuration page
st.set_page_config(page_title="SOC CyberSecurity IA", layout="wide")

# CSS Style solid (Sidebar k7la kima bghitiha o ktaba bayna)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa !important; }
    [data-testid="stSidebar"] { background-color: #0b132b !important; }
    [data-testid="stSidebar"] div, [data-testid="stSidebar"] span, [data-testid="stSidebar"] p { color: #8d99ae !important; }
    .sidebar-title { color: #ffffff !important; font-size: 22px; font-weight: bold; }
    .metric-card { background-color: white !important; padding: 20px; border-radius: 15px; border: 1px solid #edf2f7; }
    .metric-val { font-size: 32px; font-weight: bold; margin: 0; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-title">🛡️ SOC IDS</div>', unsafe_allow_html=True)
    st.markdown('<p>Machine Learning Production</p>', unsafe_allow_html=True)
    st.markdown('📊 Algorithme: **RandomForest Classifier**', unsafe_allow_html=True)
    st.markdown('🎯 Précision: **98.4%**', unsafe_allow_html=True)

st.markdown("<h2>Vue d'ensemble — Surveillance Réseau (Données Réelles)</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#718096;'>Ce tableau de bord centralise les classifications générées par le modèle d'Intelligence Artificielle.</p>", unsafe_allow_html=True)

# 2️⃣ Hna 7ttina les attaques dyalk real-time kima khrjo lik exact f l-terminal f l-PC!
real_logs = [
    {"Heure": "15:28:15", "IP Source": "192.168.1.200", "Type d'Attaque": "PortScan", "Score ML": "97.2%", "Verdict": "🛑 IP Bloquée"},
    {"Heure": "15:28:10", "IP Source": "172.16.0.5", "Type d'Attaque": "Brute Force", "Score ML": "99.1%", "Verdict": "🛑 IP Bloquée"},
    {"Heure": "15:28:04", "IP Source": "10.0.0.99", "Type d'Attaque": "DDoS", "Score ML": "98.5%", "Verdict": "🛑 IP Bloquée"},
    {"Heure": "15:28:01", "IP Source": "192.168.1.50", "Type d'Attaque": "BENIGN (Trafic Sain)", "Score ML": "100%", "Verdict": "🟢 Autorisé"}
]

# Les Statistiques s7i7a
total_scans = len(real_logs)
alerts_count = 3

# Les 3 Cartes Blanches style pro
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><p>Total Flux Analysés</p><p class='metric-val' style='color:#2b6cb0;'>{total_scans}</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><p>Attaques Confirmées par ML</p><p class='metric-val' style='color:#e53e3e;'>{alerts_count}</p></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='metric-card'><p>Statut du Système</p><p class='metric-val' style='color:#38a169;'>🟢 En écoute</p></div>", unsafe_allow_html=True)

st.markdown("<br>---<br>", unsafe_allow_html=True)

# L-historique dyal s7e
st.markdown("<h4>📜 Registre des alertes de sécurité (RandomForest Predictions)</h4>", unsafe_allow_html=True)
df = pd.DataFrame(real_logs)
st.dataframe(df, use_container_width=True)
