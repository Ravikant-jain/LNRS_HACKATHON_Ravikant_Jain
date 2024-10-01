import streamlit as st

def show():
    st.title("Welcome to the Multipage Streamlit App")
    st.write("""
        This app allows you to:
        - Process images and text on the Image Processing page.
        - Encrypt or Decrypt images on the Encryption/Decryption page.
    """)
