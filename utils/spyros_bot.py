import json
from openai import OpenAI

class SpyrosBot:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"

    # ----------------------------
    # 1. STEP: ANALYSIS ONLY
    # ----------------------------
    def analyze(self, user_input: str) -> dict:
        prompt = f"""
Είσαι AI Pre-Sales Engineer.

Ανάλυσε το παρακάτω αίτημα και επέστρεψε ΜΟΝΟ JSON.

Αίτημα:
{user_input}

ΚΑΝΕ:
- Κατηγοριοποίηση σε:
  Web Scraping / Data Collection / Excel & Reporting / AI Workflows / Custom Python Scripts
- Εκτίμηση confidence (0-1)
- Missing fields για φόρμα

ΜΟΝΟ JSON:
{
  "service_category": "",
  "confidence": 0.0,
  "missing_fields": []
}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a precise classification engine."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        try:
            return json.loads(response.choices[0].message.content)
        except:
            return {
                "service_category": "Unknown",
                "confidence": 0.0,
                "missing_fields": []
            }

    # ----------------------------
    # 2. STEP: FINAL REPORT
    # ----------------------------
    def finalize(self, form_data: dict) -> dict:
        prompt = f"""
Μετέτρεψε τα παρακάτω δεδομένα σε structured automation report JSON για την εταιρεία Does4U.

Δεδομένα:
{json.dumps(form_data, ensure_ascii=False)}

ΚΑΝΕ:
- Καθαρισμό δεδομένων
- Συμπλήρωση λογικών πεδίων μόνο αν είναι ξεκάθαρο
- ΜΗΝ εφευρίσκεις δεδομένα

ΕΠΙΣΤΡΟΦΗ ΜΟΝΟ JSON:

{
  "service_category": "",
  "confidence": 0.0,
  "name": "",
  "email": "",
  "company": "",
  "problem_description": "",
  "current_process": "",
  "desired_outcome": "",
  "websites": [],
  "documents": [],
  "estimated_volume": "",
  "additional_notes": ""
}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a strict JSON generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )

        try:
            return json.loads(response.choices[0].message.content)
        except:
            return form_data