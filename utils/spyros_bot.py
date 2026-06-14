import streamlit as st
import google.generativeai as genai
from utils.prompts import SYSTEM_PROMPT

class SpyrosBot:
    def __init__(self):
        # Σύνδεση με το Gemini χρησιμοποιώντας το Secret
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash") # Το flash είναι ιδανικό για chat
        self.chat_session = self.model.start_chat(history=[
            {"role": "user", "parts": [SYSTEM_PROMPT]},
            {"role": "model", "parts": ["Κατάλαβα. Είμαι ο Σπύρος και είμαι έτοιμος να βοηθήσω τον πελάτη."]}
        ])

    def chat(self, user_input, history):
        # Αποστολή ερωτήματος στο Gemini
        response = self.chat_session.send_message(user_input)
        return response.text