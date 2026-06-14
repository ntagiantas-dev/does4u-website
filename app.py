import streamlit as st
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.spyros_bot import SpyrosBot

# --- 1. Συνάρτηση Αποστολής Email ---
def send_lead_to_brevo(lead_data):
    try:
        smtp_server = "smtp-relay.brevo.com"
        port = 587
        sender_email = st.secrets["BREVO_LOGIN"]
        password = st.secrets["BREVO_SMTP_KEY"]
        receiver_email = "does4u.ceo@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Νέο Lead από τον Σπύρο!"
        
        body = f"Νέα δεδομένα lead:\n\n{json.dumps(lead_data, indent=4, ensure_ascii=False)}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Σφάλμα αποστολής: {e}")
        return False

# --- 2. UI & Chat ---
st.set_page_config(page_title="Does4U", layout="centered")
st.title("Does4U - Automation Solution")

if "spyros" not in st.session_state:
    st.session_state.spyros = SpyrosBot()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "lead_confirmed" not in st.session_state:
    st.session_state.lead_confirmed = False

with st.sidebar:
    st.header("Μίλα με τον Σπύρο")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Περίγραψε το πρόβλημά σου..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)

        response = st.session_state.spyros.get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# --- 3. Handover Logic ---
# Εδώ ελέγχουμε αν ο Σπύρος τελείωσε (π.χ. αν υπάρχει μέθοδος is_finished)
if hasattr(st.session_state.spyros, 'is_finished') and st.session_state.spyros.is_finished:
    if not st.session_state.lead_confirmed:
        st.subheader("Επιβεβαίωση Στοιχείων")
        data = st.session_state.spyros.get_report() # ΑΛΛΑΞΕ ΤΟ ΑΝ Η ΜΕΘΟΔΟΣ ΛΕΓΕΤΑΙ ΑΛΛΙΩΣ
        st.table(data)
        
        if st.button("Επιβεβαίωση και Αποστολή στην ομάδα"):
            if send_lead_to_brevo(data):
                st.session_state.lead_confirmed = True
                st.success("Ευχαριστούμε! Τα στοιχεία στάλθηκαν στην ομάδα μας.")
                st.rerun()

    else:
        st.info("Το αίτημά σας έχει καταχωρηθεί! Η ομάδα μας θα επικοινωνήσει μαζί σας με το demo σας εντός 2-3 εργάσιμων ημερών.")