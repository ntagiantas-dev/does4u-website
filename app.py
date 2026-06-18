Y
import streamlit as st
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.spyros_bot import SpyrosBot
 
# --- 1. Ρύθμιση Σελίδας ---
st.set_page_config(
    page_title="Does4U | Automation Solutions",
    layout="wide",
    initial_sidebar_state="expanded"
)
 
# --- 2. Premium Dark CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500&display=swap');
 
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0D1117;
        color: #E6EDF3;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stAppViewContainer"] > .main { background-color: #0D1117; }
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stDecoration"] { display: none; }
 
    [data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #21262D;
    }
    [data-testid="stSidebar"] * { color: #E6EDF3 !important; }
 
    [data-testid="stTabs"] button {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        font-size: 0.95rem;
        color: #8B949E !important;
        background: transparent;
        border: none;
        padding: 10px 20px;
        letter-spacing: 0.03em;
    }
    [data-testid="stTabs"] button[aria-selected="true"] {
        color: #FFD43B !important;
        border-bottom: 2px solid #FFD43B !important;
    }
    [data-testid="stTabs"] [data-baseweb="tab-list"] {
        border-bottom: 1px solid #21262D;
        gap: 8px;
    }
 
    .hero-eyebrow {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #3776AB;
        margin-bottom: 16px;
    }
    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3.2rem;
        font-weight: 700;
        line-height: 1.1;
        color: #E6EDF3;
        margin-bottom: 20px;
    }
    .hero-title span { color: #FFD43B; }
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.15rem;
        font-weight: 300;
        color: #8B949E;
        line-height: 1.6;
        margin-bottom: 40px;
        max-width: 560px;
    }
 
    .services-label {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #3776AB;
        margin-bottom: 20px;
    }
    .service-item {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 14px 18px;
        margin-bottom: 10px;
        background: #161B22;
        border: 1px solid #21262D;
        border-radius: 8px;
    }
    .service-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.75rem;
        font-weight: 700;
        color: #3776AB;
        min-width: 24px;
    }
    .service-name {
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        color: #E6EDF3;
    }
 
    .divider { border: none; border-top: 1px solid #21262D; margin: 40px 0; }
 
    .footer-slogan {
        text-align: center;
        padding: 40px 20px;
        border-top: 1px solid #21262D;
        margin-top: 60px;
    }
    .footer-slogan p {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.1rem;
        font-weight: 500;
        color: #8B949E;
        letter-spacing: 0.02em;
    }
    .footer-slogan span { color: #FFD43B; font-weight: 700; }
 
    .coming-soon { text-align: center; padding: 80px 20px; }
    .coming-soon h2 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.8rem;
        color: #21262D;
        margin-bottom: 12px;
    }
    .coming-soon p { color: #8B949E; font-size: 0.95rem; }
 
    .handover-card {
        background: #161B22;
        border: 1px solid #21262D;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 16px;
    }
    .handover-label {
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #3776AB;
        margin-bottom: 4px;
    }
    .handover-value { font-size: 1rem; color: #E6EDF3; }
 
    [data-testid="stChatInputTextArea"] {
        background-color: #21262D !important;
        color: #E6EDF3 !important;
        border: 1px solid #30363D !important;
        border-radius: 8px !important;
    }
    [data-testid="stButton"] > button {
        background-color: #3776AB !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        padding: 10px 24px !important;
    }
    </style>
""", unsafe_allow_html=True)
 
# --- 3. Email Logic ---
def send_lead_to_brevo(lead_data):
    try:
        sender_email = st.secrets["BREVO_LOGIN"]
        password = st.secrets["BREVO_SMTP_KEY"]
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = "does4u.ceo@gmail.com"
        msg['Subject'] = "Νέο Lead από τον Σπύρο!"
        msg.attach(MIMEText(json.dumps(lead_data, indent=4, ensure_ascii=False), 'plain'))
        server = smtplib.SMTP("smtp-relay.brevo.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, "does4u.ceo@gmail.com", msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Σφάλμα αποστολής: {e}")
        return False
 
# --- 4. Session State ---
if "spyros" not in st.session_state:
    st.session_state.spyros = SpyrosBot()
    st.session_state.messages = [
        {"role": "assistant", "content": st.session_state.spyros.get_greeting()}
    ]
if "lead_confirmed" not in st.session_state:
    st.session_state.lead_confirmed = False
 
# --- 5. Sidebar ---
with st.sidebar:
    st.markdown("### 💬 Μίλα με τον Σπύρο")
    st.caption("Pre-sales Engineer · Does4U")
    st.markdown("<hr style='border-color:#21262D'>", unsafe_allow_html=True)
 
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
 
    if not st.session_state.spyros.is_finished:
        if prompt := st.chat_input("Περίγραψε το πρόβλημά σου..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                with st.spinner(""):
                    response = st.session_state.spyros.get_response(prompt)
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    else:
        st.chat_input("Η συνομιλία ολοκληρώθηκε ✓", disabled=True)
 
# --- 6. Tabs ---
tab_main, tab_blog, tab_demos = st.tabs(["Main", "Blog", "Demos"])
 
with tab_main:
    if st.session_state.spyros.is_finished:
        st.markdown("## 📋 Report")
        if not st.session_state.lead_confirmed:
            data = st.session_state.spyros.get_report()
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f'<div class="handover-card"><div class="handover-label">Όνομα</div><div class="handover-value">{data.get("name", "-")}</div></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="handover-card"><div class="handover-label">Email</div><div class="handover-value">{data.get("email", "-")}</div></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="handover-card"><div class="handover-label">Εταιρεία</div><div class="handover-value">{data.get("company", "-")}</div></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="handover-card"><div class="handover-label">Εκτιμώμενος Όγκος</div><div class="handover-value">{data.get("estimated_volume", "-")}</div></div>', unsafe_allow_html=True)
            with col_b:
                st.markdown(f'<div class="handover-card"><div class="handover-label">Τρέχουσα Διαδικασία</div><div class="handover-value">{data.get("current_process", "-")}</div></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="handover-card"><div class="handover-label">Επιθυμητό Αποτέλεσμα</div><div class="handover-value">{data.get("desired_outcome", "-")}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="handover-card"><div class="handover-label">Περιγραφή</div><div class="handover-value">{data.get("problem_description", "-")}</div></div>', unsafe_allow_html=True)
            if data.get("additional_notes"):
                st.markdown(f'<div class="handover-card"><div class="handover-label">Σημειώσεις</div><div class="handover-value">{data.get("additional_notes", "-")}</div></div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("✅ Επιβεβαίωση και Αποστολή"):
                with st.spinner("Αποστολή..."):
                    if send_lead_to_brevo(data):
                        st.session_state.lead_confirmed = True
                        st.rerun()
        else:
            st.success("✅ Το αίτημά σας στάλθηκε! Θα επικοινωνήσουμε εντός 2-5 εργάσιμων ημερών με demo και κοστολόγηση.")
    else:
        st.markdown('<p class="hero-eyebrow">Python · AI · Automation</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Automation Solutions<br>for <span>Any Business</span></h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">We automate repetitive tasks using Python, AI and custom integrations — so your team focuses on what actually matters.</p>', unsafe_allow_html=True)
        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.markdown('<p class="services-label">What we can automate</p>', unsafe_allow_html=True)
 
        services = [
            ("01", "Web Scraping"),
            ("02", "Excel & Reporting"),
            ("03", "Data Collection"),
            ("04", "AI Workflows"),
            ("05", "Custom Python Scripts"),
        ]
        for num, name in services:
            st.markdown(f'<div class="service-item"><span class="service-number">{num}</span><span class="service-name">{name}</span></div>', unsafe_allow_html=True)
 
        st.markdown('<div class="footer-slogan"><p>You do business. <span>Does4U</span> does the repetitive work.</p></div>', unsafe_allow_html=True)
 
with tab_blog:
    st.markdown('<div class="coming-soon"><h2>Coming Soon</h2><p>Άρθρα, οδηγοί και case studies για automation.</p></div>', unsafe_allow_html=True)
 
with tab_demos:
    st.markdown('<div class="coming-soon"><h2>Coming Soon</h2><p>Live demos των υπηρεσιών μας.</p></div>', unsafe_allow_html=True)
