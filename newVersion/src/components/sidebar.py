import streamlit as st
from src.config.routing import ROUTES

# Barra lateral
def create_sidebar():
    
    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    for key, label, _ in ROUTES:
        if st.sidebar.button(label):
            st.session_state["page"] = key

    return st.session_state["page"]