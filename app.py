import streamlit as st
from utils.spyros_bot import SpyrosBot

# 1. Ρύθμιση Σελίδας
st.set_page_config(page_title="Does4U", layout="centered")

# 2. Landing Page Περιεχόμενο (Κεντρική σελίδα)
st.title("Does4U")
st.header("Automation Solution for Small Businesses")

st.subheader("What we can automate:")
st.markdown("""
- ▪︎ Web Scraping
- ▪︎ Excel and Reporting
- ▪︎ Data Collection
- ▪︎ AI Workflows
- ▪︎ Custom Python Scripts
""")

st.markdown("---")
st.markdown("### **You do Businesses. DOES4U does the Repetitive work.**")
st.markdown("---")

# 3. Sidebar Chat με τον Σπύρο
with st.sidebar:
    st.header("Μίλα με τον Σπύρο")
    
    # Αρχικοποίηση Σπύρου αν δεν υπάρχει
    if "spyros" not in st.session_state:
        st.session_state.spyros = SpyrosBot()
    
    # Διαχείριση ιστορικού μηνυμάτων
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Εμφάνιση ιστορικού
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input χρήστη
    if prompt := st.chat_input("Περίγραψε το πρόβλημά σου..."):
        # Εμφάνιση μηνύματος χρήστη
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Απόκριση Σπύρου (API Call)
        response = st.session_state.spyros.get_response(prompt)
        
        # Εμφάνιση απάντησης Σπύρου
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})