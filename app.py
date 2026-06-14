import streamlit as st
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.spyros_bot import SpyrosBot

# --- 1. Ρύθμιση Σελίδας ---
st.set_page_config(page_title="Does4U | Automation Solutions", layout="wide")

# --- 2. Styling (CSS) ---
st.markdown("""
    <style>
    .main-title { font-size: 3rem; color: #2E86C1; text-align: center; }
    .sub-header { font-size: 1.5rem; color: #566573; text-align: center; margin-bottom: 2rem; }
    .card { background-color: #F8F9F9; padding: 20px; border-radius: 10px; border-left: 5px solid #2E86C1; }
    </style>
""", unsafe_allow_html=True)

# --- 3. Landing Page ---
st.markdown('<p class="main-title">Does4U</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Automating the tedious, so you can focus on growth.</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("### Why Automate?")
    st.write("Οι επαναλαμβανόμενες εργασίες τρώνε τον χρόνο σου. Εμείς χτίζουμε το ψηφιακό σου 'χέρι'.")
    st.markdown("* **Data Accuracy:** Τέλος στα λάθη.\n* **Speed:** Δουλειά ημερών σε λεπτά.\n* **Scalability:** Συστήματα που δουλεύουν 24/7.")
with col2:
    st.markdown('<div class="card">### Our Expertise\n🔹 Web Scraping\n🔹 Excel Automation\n🔹 AI Workflows\n🔹 Custom Scripts</div>', unsafe_allow_html=True)

st.markdown("---")

# --- 4. Logic & Email ---
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
    except: return False

# --- 5. Sidebar Chat (Spyros) ---
if "spyros" not in st.session_state: st.session_state.spyros = SpyrosBot()
if "messages" not in st.session_state: st.session_state.messages = []
if "lead_confirmed" not in st.session_state: st.session_state.lead_confirmed = False

with st.sidebar:
    st.header("Μίλα με τον Σπύρο")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    if prompt := st.chat_input("Περίγραψε το πρόβλημά σου..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        response = st.session_state.spyros.get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# --- 6. Handover Logic ---
if hasattr(st.session_state.spyros, 'is_finished') and st.session_state.spyros.is_finished:
    if not st.session_state.lead_confirmed:
        data = st.session_state.spyros.get_report()
        st.table(data)
        if st.button("Επιβεβαίωση και Αποστολή"):
            if send_lead_to_brevo(data):
                st.session_state.lead_confirmed = True
                st.rerun()
    else:
        st.success("Ευχαριστούμε! Η ομάδα της Does4U θα επικοινωνήσει μαζί σας εντός 2-3 εργάσιμων ημερών με το demo σας.")import streamlit as st
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.spyros_bot import SpyrosBot

# --- 1. Ρύθμιση Σελίδας ---
st.set_page_config(page_title="Does4U | Automation Solutions", layout="wide")

# --- 2. Styling (CSS) ---
st.markdown("""
    <style>
    .main-title { font-size: 3rem; color: #2E86C1; text-align: center; }
    .sub-header { font-size: 1.5rem; color: #566573; text-align: center; margin-bottom: 2rem; }
    .card { background-color: #F8F9F9; padding: 20px; border-radius: 10px; border-left: 5px solid #2E86C1; }
    </style>
""", unsafe_allow_html=True)

# --- 3. Landing Page ---
st.markdown('<p class="main-title">Does4U</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Automating the tedious, so you can focus on growth.</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("### Why Automate?")
    st.write("Οι επαναλαμβανόμενες εργασίες τρώνε τον χρόνο σου. Εμείς χτίζουμε το ψηφιακό σου 'χέρι'.")
    st.markdown("* **Data Accuracy:** Τέλος στα λάθη.\n* **Speed:** Δουλειά ημερών σε λεπτά.\n* **Scalability:** Συστήματα που δουλεύουν 24/7.")
with col2:
    st.markdown('<div class="card">### Our Expertise\n🔹 Web Scraping\n🔹 Excel Automation\n🔹 AI Workflows\n🔹 Custom Scripts</div>', unsafe_allow_html=True)

st.markdown("---")

# --- 4. Logic & Email ---
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
    except: return False

# --- 5. Sidebar Chat (Spyros) ---
if "spyros" not in st.session_state: st.session_state.spyros = SpyrosBot()
if "messages" not in st.session_state: st.session_state.messages = []
if "lead_confirmed" not in st.session_state: st.session_state.lead_confirmed = False

with st.sidebar:
    st.header("Μίλα με τον Σπύρο")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    if prompt := st.chat_input("Περίγραψε το πρόβλημά σου..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        response = st.session_state.spyros.get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# --- 6. Handover Logic ---
if hasattr(st.session_state.spyros, 'is_finished') and st.session_state.spyros.is_finished:
    if not st.session_state.lead_confirmed:
        data = st.session_state.spyros.get_report()
        st.table(data)
        if st.button("Επιβεβαίωση και Αποστολή"):
            if send_lead_to_brevo(data):
                st.session_state.lead_confirmed = True
                st.rerun()
    else:
        st.success("Ευχαριστούμε! Η ομάδα της Does4U θα επικοινωνήσει μαζί σας εντός 2-3 εργάσιμων ημερών με το demo σας.")