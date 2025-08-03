import streamlit as st

def create_sidebar():
    st.sidebar.title("🧭 Navegación", width="content")

    if st.sidebar.button("🏠 Inicio", use_container_width=True):
        st.session_state["page"] = "home"
    
    if st.sidebar.button("📈 Economía", use_container_width=True):
        st.session_state["page"] = "economy"
        
    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    return st.session_state["page"]