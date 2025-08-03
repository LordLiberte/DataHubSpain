import streamlit as st
from src.config.routing import ROUTES

# Barra lateral
def create_sidebar():

    for key, label, _ in ROUTES:
        if st.sidebar.button(label):
            st.session_state["page"] = key

    return st.session_state["page"]