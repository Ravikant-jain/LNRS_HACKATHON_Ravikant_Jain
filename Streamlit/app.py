import streamlit as st
from sections import home, image_processing, encryption_decryption

# Sidebar for navigation
st.sidebar.title("Pages:")
page = st.sidebar.radio("Go to", ["Home", "Image Processing", "Encryption/Decryption"])

# Load the selected page
if page == "Home":
    home.show()
elif page == "Image Processing":
    image_processing.show()
elif page == "Encryption/Decryption":
    encryption_decryption.show()