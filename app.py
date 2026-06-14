import streamlit as st

# Ρύθμιση σελίδας
st.set_page_config(page_title="Does4U", layout="centered")

# Κεντρικός τίτλος
st.title("Does4U")

# Επικεφαλίδα
st.header("Automation Solution for Small Businesses")

# Λίστα με υπηρεσίες
st.subheader("What we can automate:")
st.markdown("""
- ▪︎ Web Scraping
- ▪︎ Excel and Reporting
- ▪︎ Data Collection
- ▪︎ AI Workflows
- ▪︎ Custom Python Scripts
""")

# Slogan
st.markdown("---")
st.markdown("### **You do Businesses. DOES4U does the Repetitive work.**")
st.markdown("---")

# Σημείωση για τον Σπύρο (το αφήνουμε για να μην χαθεί το context)
with st.sidebar:
    st.header("Μίλα με τον Σπύρο")
    st.info("Ο Σπύρος είναι το AI μας και θα είναι διαθέσιμος σύντομα!")