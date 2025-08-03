import streamlit as st

def create_sidebar():
    st.sidebar.title("🧭 Navegación")

    if st.sidebar.button("🏠 Inicio"):
        st.session_state["page"] = "home"
    
    if st.sidebar.button("📈 Economía"):
        st.session_state["page"] = "economy"
        
    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    return st.session_state["page"]