import streamlit as st
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SpyrosBot:
    def __init__(self):
        self.is_finished = False
        self.final_data = {}
        # Εδώ θα βάλεις το logic σου για τα prompts
        
    def get_response(self, prompt):
        # Εδώ η λογική που είχες για τον Σπύρο
        # Όταν φτάσεις στο βήμα 5, κάνε:
        # self.is_finished = True
        # self.final_data = { ...τα δεδομένα σου... }
        return "Απάντηση Σπύρου..."

    def get_report(self):
        return self.final_data

def send_lead_to_brevo(lead_data):
    try:
        msg = MIMEMultipart()
        msg['From'] = st.secrets["BREVO_LOGIN"]
        msg['To'] = "does4u.ceo@gmail.com"
        msg['Subject'] = "Νέο Lead από τον Σπύρο!"
        msg.attach(MIMEText(json.dumps(lead_data, indent=4), 'plain'))
        server = smtplib.SMTP("smtp-relay.brevo.com", 587)
        server.starttls()
        server.login(st.secrets["BREVO_LOGIN"], st.secrets["BREVO_SMTP_KEY"])
        server.sendmail(st.secrets["BREVO_LOGIN"], "does4u.ceo@gmail.com", msg.as_string())
        server.quit()
        return True
    except:
        return False