import streamlit as st
import google.generativeai as genai
from utils.prompts import SYSTEM_PROMPT

class SpyrosBot:
    def __init__(self):
        # Σύνδεση με το Gemini
        try:
            st.sidebar.write("DEBUG: Προσπάθεια σύνδεσης...")
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
            
            self.chat_session = self.model.start_chat(history=[
                {"role": "user", "parts": [SYSTEM_PROMPT]},
                {"role": "model", "parts": ["Κατάλαβα. Είμαι ο Σπύρος, αναλυτής της Does4U. Είμαι έτοιμος."]}
            ])
            st.sidebar.write("DEBUG: Σύνδεση επιτυχής!")
        except Exception as e:
            st.sidebar.error(f"DEBUG Error: {e}")

    def get_response(self, user_input):
        try:
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Σφάλμα επικοινωνίας: {e}"