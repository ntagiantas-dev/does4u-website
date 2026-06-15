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
    st.markdown('<div class="card">### Our Expertise<br>🔹 Web Scraping<br>🔹 Excel Automation<br>🔹 AI Workflows<br>🔹 Custom Scripts</div>', unsafe_allow_html=True)

st.markdown("---")

# --- 4. Email Logic ---
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

# --- 5. Session State Initialization ---
if "spyros" not in st.session_state:
    st.session_state.spyros = SpyrosBot()
    # Το πρώτο μήνυμα (greeting) έχει ήδη δημιουργηθεί στο __init__
    # Το προσθέτουμε στα messages για εμφάνιση
    st.session_state.messages = [
        {"role": "assistant", "content": st.session_state.spyros.get_greeting()}
    ]

if "lead_confirmed" not in st.session_state:
    st.session_state.lead_confirmed = False

# --- 6. Sidebar Chat ---
with st.sidebar:
    st.header("💬 Μίλα με τον Σπύρο")
    st.caption("Pre-sales Engineer · Does4U")

    # Εμφάνιση ιστορικού
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input πελάτη (disabled αν έχει ολοκληρωθεί)
    if not st.session_state.spyros.is_finished:
        if prompt := st.chat_input("Γράψε εδώ..."):
            # Εμφάνιση μηνύματος χρήστη
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Απάντηση Σπύρου
            with st.chat_message("assistant"):
                with st.spinner("Ο Σπύρος σκέφτεται..."):
                    response = st.session_state.spyros.get_response(prompt)
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

            st.rerun()
    else:
        st.chat_input("Η συνομιλία ολοκληρώθηκε ✓", disabled=True)

# --- 7. Handover Logic (Main Area) ---
if st.session_state.spyros.is_finished:
    st.markdown("## 📋 Report Πελάτη")

    if not st.session_state.lead_confirmed:
        data = st.session_state.spyros.get_report()

        # Εμφάνιση δεδομένων σε καθαρή μορφή
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**👤 Όνομα:** {data.get('name', '-')}")
            st.markdown(f"**📧 Email:** {data.get('email', '-')}")
            st.markdown(f"**🏢 Εταιρεία:** {data.get('company', '-')}")
            st.markdown(f"**📊 Εκτιμώμενος Όγκος:** {data.get('estimated_volume', '-')}")
        with col_b:
            st.markdown(f"**🔧 Τρέχουσα Διαδικασία:** {data.get('current_process', '-')}")
            st.markdown(f"**🎯 Επιθυμητό Αποτέλεσμα:** {data.get('desired_outcome', '-')}")

        st.markdown(f"**📝 Περιγραφή Προβλήματος:** {data.get('problem_description', '-')}")

        if data.get('additional_notes'):
            st.markdown(f"**💡 Επιπλέον Σημειώσεις:** {data.get('additional_notes', '-')}")

        st.markdown("---")
        st.markdown("**Raw JSON:**")
        st.json(data)

        if st.button("✅ Επιβεβαίωση και Αποστολή στην Ομάδα", type="primary"):
            with st.spinner("Αποστολή..."):
                if send_lead_to_brevo(data):
                    st.session_state.lead_confirmed = True
                    st.rerun()
    else:
        st.success("""
        ✅ **Το αίτημά σας στάλθηκε επιτυχώς!**
        
        Η ομάδα της Does4U έλαβε τις πληροφορίες σας.
        Θα επικοινωνήσουμε μαζί σας εντός **2-5 εργάσιμων ημερών** με:
        
        - 🎬 **Demo** της προτεινόμενης λύσης
        - 💰 **Κοστολόγηση** βάσει των απαιτήσεών σας
        
        Ευχαριστούμε που επιλέξατε την **Does4U**!
        """)