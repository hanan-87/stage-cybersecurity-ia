import streamlit as st
import pandas as pd

# Configuration dyal l-page 
st.set_page_config(page_title="SOC CyberSecurity IA", layout="wide", initial_sidebar_state="expanded")

# CSS 100% M9add bach i-forci l-sidebar t-koun k7la o l-ktaba t-ban bayna
st.markdown("""
    <style>
    /* Background dyal l-page complete */
    .main { background-color: #f8f9fa !important; }
    
    /* Forcer l-sidebar t-koun k7la kima f image_d80866.png */
    [data-testid="stSidebar"] { 
        background-color: #0b132b !important; 
    }
    
    /* Hada houwa l-guelb dial l-moshkil: forcer l-ktaba dial l-sidebar t-welli bayna */
    [data-testid="stSidebar"] div, [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] h2 {
        color: #8d99ae !important;
    }
    
    /* Masquer le menu par défaut de Streamlit */
    div[data-testid="stSidebarNav"] { display: none !important; }
    
    /* Style dial les sections o titles f l-sidebar */
    .sidebar-title { color: #ffffff !important; font-size: 22px; font-weight: bold; padding-top: 10px; margin-bottom: 0px; }
    .sidebar-subtitle { color: #5c6b73 !important; font-size: 13px; margin-top: 0px; margin-bottom: 25px; }
    .sidebar-section { color: #4dabf7 !important; font-weight: bold; font-size: 11px; margin-top: 25px; margin-bottom: 10px; letter-spacing: 1px; }
    
    /* Éléments aktif o menu text */
    .menu-item-active { 
        color: #ffffff !important; font-size: 15px; padding: 10px 15px; 
        background-color: #1c2541 !important; border-radius: 8px; font-weight: bold;
        margin-left: -5px; display: block;
    }
    .menu-item { color: #a2a8d3 !important; font-size: 15px; padding: 10px 10px; display: block; }
    
    /* Footer dial l-agent active */
    .sidebar-footer { margin-top: 40px; padding: 10px; border-top: 1px solid #1c2541; }
    .agent-status { color: #2ecc71 !important; font-weight: bold; font-size: 14px; }
    .agent-sub { color: #5c6b73 !important; font-size: 11px; }

    /* Cards dial metrics l-wst */
    .metric-card {
        background-color: white !important; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03); border: 1px solid #edf2f7;
    }
    .metric-title { color: #718096 !important; font-size: 14px; margin-bottom: 5px; }
    .metric-val { font-size: 32px; font-weight: bold; margin: 0; }
    </style>
""", unsafe_allow_html=True)

# 3️⃣ SIDEBAR HTML (Daba ghadi t-ban solid 100%)
with st.sidebar:
    st.markdown('<div class="sidebar-title">🛡️ SOC IDS</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Hanan Agent API</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">PRINCIPAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item-active">📊 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🔔 Alertes IA</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">SYSTEME</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🟢 Agent Connecté</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-footer"><div class="agent-status">🟢 API Active — Cloud</div><div class="agent-sub">FastAPI + Machine Learning</div></div>', unsafe_allow_html=True)

# 4️⃣ MAIN CONTENT 
st.markdown("<h2>Vue d'ensemble — Surveillance IA</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#718096;'>Analyse du trafic réseau en temps réel via Hugging Face</p>", unsafe_allow_html=True)

if "total_scans" not in st.session_state: st.session_state.total_scans = 0
if "alerts_count" not in st.session_state: st.session_state.alerts_count = 0
if "incidents_list" not in st.session_state: st.session_state.incidents_list = []

# Les 3 Cartes Blanches
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><p class='metric-title'>Trafic Total Scanné</p><p class='metric-val' style='color:#2b6cb0;'>{st.session_state.total_scans}</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><p class='metric-title'>Attaques Détectées</p><p class='metric-val' style='color:#e53e3e;'>{st.session_state.alerts_count}</p></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='metric-card'><p class='metric-title'>Statut du Système</p><p class='metric-val' style='color:#38a169;'>100%</p></div>", unsafe_allow_html=True)

st.markdown("<br>---<br>", unsafe_allow_html=True)

st.markdown("<h4>📜 Historique des Détections de votre API</h4>", unsafe_allow_html=True)

if len(st.session_state.incidents_list) == 0:
    st.info("En attente de trafic depuis l'agent local...")
else:
    df = pd.DataFrame(st.session_state.incidents_list)
    st.dataframe(df, use_container_width=True)
