import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_lead_to_brevo(lead_data):
    # Στοιχεία από τα secrets σου
    smtp_server = "smtp-relay.brevo.com"
    port = 587
    sender_email = st.secrets["BREVO_LOGIN"]  # Το login που είδαμε στο Brevo
    password = st.secrets["BREVO_SMTP_KEY"]   # Το νέο κλειδί που έφτιαξες
    receiver_email = "does4u.ceo@gmail.com"

    # Δημιουργία μηνύματος
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Νέο Lead από τον Σπύρο!"
    
    body = f"Βρέθηκε ένα νέο lead με τα παρακάτω δεδομένα:\n\n{lead_data}"
    msg.attach(MIMEText(body, 'plain'))

    # Αποστολή μέσω Brevo SMTP
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Σφάλμα κατά την αποστολή: {e}")
        return False

# --- Πώς θα το χρησιμοποιείς στο τέλος των 5 βημάτων σου ---
# Αν υποθέσουμε ότι το json_data είναι το τελικό σου αρχείο:
# if st.button("Αποστολή Lead"):
#     success = send_lead_to_brevo(str(json_data))
#     if success:
#         st.success("Το lead στάλθηκε με επιτυχία στο email σου!")