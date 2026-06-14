import streamlit as st
import google.generativeai as genai
from utils.prompts import SYSTEM_PROMPT

class SpyrosBot:
    def __init__(self):
        # Χρήση του μοντέλου που είδαμε στο AI Studio
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel("gemini-3-flash-preview")
        
        # Έναρξη chat με το system prompt ως αρχική οδηγία
        self.chat_session = self.model.start_chat(history=[
            {"role": "user", "parts": [SYSTEM_PROMPT]},
            {"role": "model", "parts": ["Κατάλαβα. Είμαι ο Σπύρος, ο Pre-sales Engineer της Does4U. Είμαι έτοιμος να βοηθήσω τον πελάτη και να συλλέξω τα δεδομένα για το demo."]}
        ])

    def get_response(self, user_input):
        try:
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Σφάλμα: {str(e)}"