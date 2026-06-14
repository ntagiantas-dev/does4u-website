import streamlit as st
import google.generativeai as genai
from utils.prompts import SYSTEM_PROMPT

class SpyrosBot:
    def __init__(self):
        # Σύνδεση με το Gemini χρησιμοποιώντας το Secret
        # Προσοχή: Το όνομα στο st.secrets πρέπει να είναι ακριβώς το ίδιο με αυτό που έβαλες στο Cloud
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Ξεκινάμε το chat session με το system prompt
        self.chat_session = self.model.start_chat(history=[
            {"role": "user", "parts": [SYSTEM_PROMPT]},
            {"role": "model", "parts": ["Κατάλαβα. Είμαι ο Σπύρος, αναλυτής της Does4U. Είμαι έτοιμος."]}
        ])

    def get_response(self, user_input):
        # Στέλνουμε το ερώτημα στο API
        response = self.chat_session.send_message(user_input)
        return response.text