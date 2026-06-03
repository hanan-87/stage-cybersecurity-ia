import streamlit as st
import pandas as pd
import requests

# 1️⃣ Configuration dyal l-page style SOC Pro
st.set_page_config(page_title="SOC CyberSecurity IA", layout="wide", initial_sidebar_state="expanded")

# 2️⃣ CSS Custom bach n-baddlou l-Sidebar o l-cards 100% f-7al image_d80866.png
st.markdown("""
    <style>
    /* Background dyal l-page */
    .main { background-color: #f8f9fa; }
    
    /* Style dial l-Sidebar (La barre sombre à gauche) */
    div[data-testid="stSidebar"] { 
        background-color: #0b132b !important; 
        min-width: 280px !important;
    }
    
    /* Masquer le menu par défaut de Streamlit */
    div[data-testid="stSidebarNav"] { display: none !important; }
    
    /* Textes f l-Sidebar */
    .sidebar-title { color: white; font-size: 22px; font-weight: bold; padding-top: 10px; }
    .sidebar-subtitle { color: #5c6b73; font-size: 13px; margin-bottom: 25px; }
    .sidebar-section { color: #3a4764; font-weight: bold; font-size: 11px; margin-top: 25px; margin-bottom: 10px; letter-spacing: 1px; }
    
    /* Éléments dyal l-menu k7el */
    .menu-item { color: #8d99ae; font-size: 15px; padding: 10px 0; }
    .menu-item-active { 
        color: white !important; font-size: 15px; padding: 10px 15px; 
        background-color: #1c2541; border-radius: 8px; font-weight: bold;
        margin-left: -10px;
    }
    
    /* L-blassa l-khdra dyal l-Agent active f l-te7t */
    .sidebar-footer { position: fixed; bottom: 20px; left: 20px; width: 240px; }
    .agent-status { color: #2ecc71; font-weight: bold; font-size: 14px; }
    .agent-sub { color: #5c6b73; font-size: 11px; }

    /* Design dyal les cartes l-byadin kima f l-image */
    .metric-card {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03); border: 1px solid #edf2f7;
    }
    .metric-title { color: #718096; font-size: 14px; margin-bottom: 5px; }
    .metric-val { font-size: 32px; font-weight: bold; margin: 0; }
    </style>
""", unsafe_allow_html=True)

# 3️⃣ SIDEBAR (Ghir l-Style li k7el f-7al l-image)
with st.sidebar:
    st.markdown('<div class="sidebar-title">📘 SOC IDS</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Hanan Agent API</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">PRINCIPAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item-active">📊 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🔔 Alertes IA</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">SYSTEME</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🟢 Agent Connecté</div>', unsafe_allow_html=True)
    
    # Footer f l-te7t dial l-sidebar kima f l-image
    st.markdown('<div class="sidebar-footer"><div class="agent-status">🟢 API Active — Cloud</div><div class="agent-sub">FastAPI + Machine Learning</div></div>', unsafe_allow_html=True)

# 4️⃣ MAIN CONTENT (Hna fin ghadi t-bda t-aficha d-data dyalk real-time)
st.markdown("<h2>Vue d'ensemble — Surveillance IA</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#718096;'>Analyse du trafic réseau en temps réel via Hugging Face</p>", unsafe_allow_html=True)

# Initialisation dyal l-base f Streamlit (Ssession State) bach n-sajlo l-incidents
if "total_scans" not in st.session_state: st.session_state.total_scans = 0
if "alerts_count" not in st.session_state: st.session_state.alerts_count = 0
if "incidents_list" not in st.session_state: st.session_state.incidents_list = []

# Les 3 Cartes Blanches f-7al l-image ghir b les informations dyalk nti:
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><p class='metric-title'>Trafic Total Scanné</p><p class='metric-val' style='color:#2b6cb0;'>{st.session_state.total_scans}</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><p class='metric-title'>Attaques Détectées</p><p class='metric-val' style='color:#e53e3e;'>{st.session_state.alerts_count}</p></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='metric-card'><p class='metric-title'>Statut du Système</p><p class='metric-val' style='color:#38a169;'>100%</p></div>", unsafe_allow_html=True)

st.markdown("<br>---<br>", unsafe_allow_html=True)

# Lesta dyal l-incidents real-time f l-te7t
st.markdown("<h4>📜 Historique des Détections de votre API</h4>", unsafe_allow_html=True)

if len(st.session_state.incidents_list) == 0:
    st.info("En attente de trafic depuis l'agent local...")
else:
    df = pd.DataFrame(st.session_state.incidents_list)
    st.dataframe(df, use_container_width=True)
