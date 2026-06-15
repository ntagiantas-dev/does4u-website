import streamlit as st
import json
import re
import google.generativeai as genai

# Ρύθμιση Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

SYSTEM_PROMPT = """
Είσαι ο Σπύρος, ο Pre-sales Engineer της Does4U. Είσαι φιλικός, επαγγελματίας και κάνεις μία ερώτηση τη φορά.
Ο στόχος σου είναι να συλλέξεις πληροφορίες για να φτιάξεις ένα report αυτοματισμού.
Ακολούθησε τα 5 βήματα (ΑΝΑΛΥΣΗ, ΚΑΤΗΓΟΡΙΟΠΟΙΗΣΗ, ΣΥΛΛΟΓΗ, REPORT, ΚΛΕΙΣΙΜΟ) όπως αναφέρονται στις οδηγίες σου.
Στο τέλος, εμφάνισε το JSON σε ```json ... ``` block. Γράφε πάντα στα Ελληνικά.
"""

class SpyrosBot:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash") # 2.5 flash αν υπάρχει διαθέσιμο, αλλιώς 1.5
        self.chat = self.model.start_chat(history=[])
        # Αρχικοποίηση με το system prompt
        self.chat.send_message(SYSTEM_PROMPT)
        
        self.is_finished = False
        self.final_data = {}
        self.history = []
        self._send_greeting()

    def _send_greeting(self):
        # Πρώτη επαφή
        response = self.chat.send_message("Καλωσόρισε τον πελάτη και ρώτα το πρόβλημά του.")
        self.history.append({"role": "assistant", "content": response.text})

    def get_response(self, user_input: str) -> str:
        self.history.append({"role": "user", "content": user_input})
        
        response = self.chat.send_message(user_input)
        bot_reply = response.text
        
        self.history.append({"role": "assistant", "content": bot_reply})
        
        # Έλεγχος αν το JSON είναι έτοιμο
        extracted = self._extract_json(bot_reply)
        if extracted:
            self.final_data = extracted
            self.is_finished = True
        
        return bot_reply

    def _extract_json(self, text: str) -> dict | None:
        pattern = r"```json\s*(\{.*?\})\s*```"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except:
                return None
        return None

    def get_report(self) -> dict:
        return self.final_data

    def get_greeting(self) -> str:
        return self.history[0]["content"] if self.history else "Γεια σου! Είμαι ο Σπύρος."