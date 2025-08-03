import streamlit as st

def create_sidebar():
    st.sidebar.title("🧭 Navegación")

    section = st.sidebar.radio("Ir a:", [
        "🏠 Inicio",
        "📈 Economía",
        "👥 Población",
        "🚆 Transporte"
    ])

    return section