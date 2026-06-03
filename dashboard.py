import streamlit as st
import pandas as pd

# Configuration dyal l-page style SOC Pro
st.set_page_config(page_title="SOC IDS Dashboard", layout="wide", initial_sidebar_state="expanded")

# CSS wa3er bach n-baddlou l-Sidebar o l-cards i-welliw 100% f-7al image_d80866.png
st.markdown("""
    <style>
    /* Background dyal l-page complète */
    .main { background-color: #f8f9fa; }
    
    /* Style dial l-Sidebar (La barre sombre à gauche) */
    div[data-testid="stSidebar"] { 
        background-color: #0b132b !important; 
        min-width: 280px !important;
        max-width: 280px !important;
    }
    
    /* M7i l-khwa dyal Streamlit l-fo9ani */
    div[data-testid="stSidebarNav"] { display: none !important; }
    
    /* Ktaba f وسط l-Sidebar */
    .sidebar-title { color: white; font-size: 22px; font-weight: bold; margin-bottom: 0px; padding-top: 10px; }
    .sidebar-subtitle { color: #5c6b73; font-size: 13px; margin-top: 0px; margin-bottom: 25px; }
    .sidebar-section { color: #3a4764; font-weight: bold; font-size: 11px; margin-top: 25px; margin-bottom: 10px; letter-spacing: 1px; }
    
    /* Les éléments dyal l-menu */
    .menu-item { color: #8d99ae; font-size: 15px; padding: 10px 0; cursor: pointer; display: flex; align-items: center; }
    .menu-item-active { 
        color: white !important; font-size: 15px; padding: 10px 15px; 
        background-color: #1c2541; border-radius: 8px; font-weight: bold;
        display: flex; align-items: center; margin-left: -10px;
    }
    
    /* L-blassa l-khdra dial l-Agent l-te7t */
    .sidebar-footer {
        position: fixed; bottom: 20px; left: 20px; width: 240px;
    }
    .agent-status { color: #2ecc71; font-weight: bold; font-size: 14px; display: flex; align-items: center; }
    .agent-sub { color: #5c6b73; font-size: 11px; margin-top: -5px; }

    /* Cards dial l-metrics l-byadin */
    .metric-card {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03); border: 1px solid #edf2f7;
        text-align: left; position: relative;
    }
    .metric-icon-box {
        position: absolute; top: 15px; left: 20px; width: 35px; height: 35px;
        background-color: #fff5f5; border-radius: 8px; display: flex; align-items: center; justify-content: center;
    }
    .metric-title { color: #718096; font-size: 14px; margin-bottom: 0px; margin-left: 0px; padding-top: 25px; }
    .metric-val { font-size: 36px; font-weight: bold; margin-top: -5px; margin-bottom: 0px; }
    .metric-sub { font-size: 12px; margin-top: -5px; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# --- 1️⃣ SIDEBAR (M-صاوبة exact b l-alwan o l-ktaba dyal l-image) ---
with st.sidebar:
    st.markdown('<div class="sidebar-title">📘 SOC IDS</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Hybrid Agent</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">PRINCIPAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item-active">📊 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🔔 Alertes</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🚫 IPs bloquées</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">ANALYSE</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📈 Statistiques</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📄 Rapports</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">SYSTÈME</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">⚙️ Paramètres</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">✉️ Emails SOC</div>', unsafe_allow_html=True)
    
    # L-partie l-te7taniya dyal l-Agent actif
    st.markdown('<br><br><br><br>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-footer">', unsafe_allow_html=True)
    st.markdown('<div class="agent-status">🟢 Agent actif — enp0s8</div>', unsafe_allow_html=True)
    st.markdown('<div class="agent-sub">Snort 2.9 + ML RandomForest</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2️⃣ MAIN CONTENT (L-wst dial l-écran) ---
col_header, col_btns, col_time = st.columns([5, 4, 1])

with col_header:
    st.markdown("<h2 style='margin-bottom:0;'>Vue d'ensemble — SOC</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#718096; margin-top:0;'>Hybrid IDS · Ubuntu router · Kali → Win10</p>", unsafe_allow_html=True)

with col_btns:
    st.markdown('<br>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.button("🚨 Simuler attaque", use_container_width=True)
    with c2: st.button("🔄 Actualiser", use_container_width=True)

with col_time:
    st.markdown('<br><div style="background-color:white; padding:10px; border-radius:8px; border:1px solid #e2e8f0; text-align:center; font-weight:bold; color:#4a5568;">15:17:34</div>', unsafe_allow_html=True)

# Les 4 Cards dyal l-metrics f-7al image_d80866.png
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='metric-card'><div class='metric-icon-box' style='background-color:#fff5f5; color:#e53e3e;'>🚫</div><p class='metric-title'>IPs bloquées</p><p class='metric-val' style='color:#e53e3e;'>1</p><p class='metric-sub' style='color:#e53e3e;'>10.0.0.20</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-card'><div class='metric-icon-box' style='background-color:#f0fff4; color:#38a169;'>📋</div><p class='metric-title'>Total alertes</p><p class='metric-val' style='color:#2d3748;'>4</p><p class='metric-sub' style='color:#38a169;'>🟢 Session active</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-card'><div class='metric-icon-box' style='background-color:#ebf8ff; color:#3182ce;'>✉️</div><p class='metric-title'>Emails envoyés</p><p class='metric-val' style='color:#3182ce;'>4</p><p class='metric-sub' style='color:#718096;'>Gmail SMTP</p></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='metric-card'><div class='metric-icon-box' style='background-color:#f0fff4; color:#38a169;'>📈</div><p class='metric-title'>Taux de blocage</p><p class='metric-val' style='color:#38a169;'>100%</p><p class='metric-sub' style='color:#38a169;'>Snort + ML actifs</p></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Sections: Graphique & Table dyal l-attacks
col_graph, col_type = st.columns([5, 3])

with col_graph:
    st.markdown("<h4>Activité des attaques <span style='font-size:13px; color:#718096; font-weight:normal;'>dernière session</span></h4>", unsafe_allow_html=True)
    chart_data = pd.DataFrame({
        'Temps': ['23:13:28', '23:30:22', '23:40:08', '23:55:48'],
        'Alertes': [1, 2, 3, 4]
    })
    st.line_chart(chart_data.set_index('Temps'), height=220)

with col_type:
    st.markdown("<h4>Attagues par type</h4>", unsafe_allow_html=True)
    st.markdown("""
        <table style='width:100%; font-size:14px; border-collapse:collapse; margin-top:15px;'>
            <tr style='height:35px;'><td>DDoS ICMP</td><td style='text-align:right; font-weight:bold; color:#e53e3e;'>████████ 4</td></tr>
            <tr style='height:35px;'><td>DoS SYN</td><td style='text-align:right; font-weight:bold; color:#dd6b20;'>████ 2</td></tr>
            <tr style='height:35px;'><td>Port Scan</td><td style='text-align:right; font-weight:bold; color:#3182ce;'>██ 1</td></tr>
            <tr style='height:35px;'><td>SSH BF</td><td style='text-align:right; font-weight:bold; color:#38a169;'>█ 1</td></tr>
        </table>
    """, unsafe_allow_html=True)

st.markdown("<br>---<br>", unsafe_allow_html=True)

# Historique f l-te7t
col_h1, col_h2 = st.columns(2)
with col_h1:
    st.markdown("<h4>📜 Historique des alertes <span style='font-size:13px; color:#718096; font-weight:normal;'>4 entrées</span></h4>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background-color:white; padding:15px; border-radius:10px; border:1px solid #e2e8f0; font-size:14px;'>
            ⏱️ <b>23:55:48</b> &nbsp;&nbsp;&nbsp;&nbsp; 🔴 <span style='color:#e53e3e;'>10.0.0.20</span> &nbsp;&nbsp;&nbsp;&nbsp; <span style='background-color:#feebc8; color:#dd6b20; padding:2px 6px; border-radius:4px;'>SSH Brute Force</span><br><hr style='margin:10px 0;'>
            ⏱️ <b>23:40:08</b> &nbsp;&nbsp;&nbsp;&nbsp; 🔴 <span style='color:#e53e3e;'>192.168.1.105</span> &nbsp;&nbsp;&nbsp;&nbsp; <span style='background-color:#fed7d7; color:#e53e3e; padding:2px 6px; border-radius:4px;'>DDoS ICMP</span>
        </div>
    """, unsafe_allow_html=True)

with col_h2:
    st.markdown("<h4>📧 Notifications email SOC</h4>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background-color:white; padding:15px; border-radius:10px; border:1px solid #e2e8f0; font-size:14px; display:flex; align-items:center;'>
            <div style='font-size:24px; margin-right:15px;'>📨</div>
            <div>
                <b>Alerte — SSH Brute Force</b><br>
                <span style='color:#718096; font-size:12px;'>IP bloquée : 10.0.0.20<br>23:55:48 · Gmail SMTP envoyé</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
