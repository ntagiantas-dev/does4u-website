import streamlit as st

# Ρύθμιση της σελίδας
st.set_page_config(page_title="Does4U", layout="wide")

# Header
st.title("Does4U")
st.subheader("We turn your chaos into automated workflows.")

# Περιεχόμενο - Εδώ θα μπει η περιγραφή της υπηρεσίας
st.write("""
### Welcome to Does4U
Εδώ βοηθάμε τις επιχειρήσεις να απαλλαγούν από τις επαναλαμβανόμενες διαδικασίες 
που τρώνε τον χρόνο τους.
""")

# Προσωρινό placeholder για τον Σπύρο στο sidebar
with st.sidebar:
    st.header("💬 Μίλα με τον Σπύρο")
    st.info("Ο Σπύρος είναι το AI μας και θα είναι διαθέσιμος σύντομα!")

# Placeholder για μελλοντικές καρτέλες
st.divider()
st.write("Σύντομα θα βρείτε εδώ το Blog μας και τα Demos μας.")