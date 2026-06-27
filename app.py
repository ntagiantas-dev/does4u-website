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

# --- 2. Premium Dark CSS (UNCHANGED) ---
st.markdown("""<style> ... (ΚΡΑΤΑΜΕ ΑΚΡΙΒΩΣ ΤΟ ΔΙΚΟ ΣΟΥ CSS) ... </style>""", unsafe_allow_html=True)


# --- 3. Email Logic (UNCHANGED) ---
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


# --- 4. SESSION STATE (NEW FLOW) ---
if "spyros" not in st.session_state:
    st.session_state.spyros = SpyrosBot(st.secrets["OPENAI_API_KEY"])

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "form_data" not in st.session_state:
    st.session_state.form_data = {}

if "lead_confirmed" not in st.session_state:
    st.session_state.lead_confirmed = False


# --- 5. SIDEBAR (NOW ONLY TRIGGER) ---
with st.sidebar:
    st.markdown("### 💬 Μίλα με τον Σπύρο")
    st.caption("Pre-sales AI · Does4U")

    prompt = st.chat_input("Περιγράψε τι θέλεις να αυτοματοποιήσεις...")

    if prompt and st.session_state.analysis is None:
        # STEP 1: ANALYZE ONLY
        analysis = st.session_state.spyros.analyze(prompt)
        st.session_state.analysis = analysis

        st.success(f"Κατηγορία: {analysis.get('service_category')}")
        st.info(f"Confidence: {analysis.get('confidence')}")

        st.rerun()

    elif st.session_state.analysis:
        st.info("Ολοκλήρωσε τη φόρμα στο Main tab →")


# --- 6. TABS ---
tab_main, tab_blog, tab_demos = st.tabs(["Main", "Blog", "Demos"])


# =========================
# MAIN TAB (FORM-FIRST CORE)
# =========================
with tab_main:

    st.markdown("## 📋 Lead Intake")

    # CASE 1: NOT STARTED
    if st.session_state.analysis is None:
        st.markdown("### 👋 Ξεκίνα περιγράφοντας τι θέλεις να αυτοματοποιήσεις από το sidebar.")

    # CASE 2: FORM MODE
    else:
        analysis = st.session_state.analysis

        st.markdown(f"### Κατηγορία: `{analysis.get('service_category')}`")
        st.markdown(f"Confidence: `{analysis.get('confidence')}`")

        st.markdown("---")

        # BASE FORM
        st.session_state.form_data["name"] = st.text_input("Ονοματεπώνυμο")
        st.session_state.form_data["email"] = st.text_input("Email")
        st.session_state.form_data["company"] = st.text_input("Εταιρεία")

        st.session_state.form_data["current_process"] = st.text_area("Τρέχουσα διαδικασία")
        st.session_state.form_data["desired_outcome"] = st.text_area("Επιθυμητό αποτέλεσμα")
        st.session_state.form_data["estimated_volume"] = st.text_input("Εκτιμώμενος όγκος")

        # DYNAMIC FIELDS
        if analysis.get("service_category") == "Web Scraping":
            st.session_state.form_data["websites"] = st.text_area("Websites (comma separated)").split(",")

        if analysis.get("service_category") == "AI Workflows":
            st.session_state.form_data["additional_notes"] = st.text_area("Workflow details")

        st.markdown("---")

        # SUBMIT
        if st.button("🚀 Δημιουργία Report"):

            # FINAL STEP (CLEAN + STRUCTURE)
            final_data = st.session_state.spyros.finalize(st.session_state.form_data)

            st.session_state.final_data = final_data
            st.session_state.lead_confirmed = False

            st.success("Report δημιουργήθηκε!")


        # SHOW REPORT
        if "final_data" in st.session_state:
            data = st.session_state.final_data

            st.markdown("## 📦 Final Report")
            st.json(data)

            if not st.session_state.lead_confirmed:
                if st.button("✅ Επιβεβαίωση & Αποστολή"):
                    if send_lead_to_brevo(data):
                        st.session_state.lead_confirmed = True
                        st.success("Στάλθηκε επιτυχώς!")
                        st.rerun()


# =========================
# BLOG TAB (UNCHANGED)
# =========================
with tab_blog:
    st.markdown("""
    <div style="text-align:center;padding:80px;">
        <h2>Coming Soon</h2>
        <p>Automation άρθρα & guides</p>
    </div>
    """, unsafe_allow_html=True)


# =========================
# DEMOS TAB (UNCHANGED)
# =========================
with tab_demos:
    st.markdown("""
    <div style="text-align:center;padding:80px;">
        <h2>Coming Soon</h2>
        <p>Live demos των υπηρεσιών Does4U</p>
    </div>
    """, unsafe_allow_html=True)