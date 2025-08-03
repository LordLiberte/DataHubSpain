import streamlit as st
from src.config.constants import INTRO_TEXT

def configpage():
    st.set_page_config(
        page_title="Open Spain Insights",
        page_icon="🇪🇸",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def show_footer():
    st.markdown("---")
    st.caption("Hecho con ❤️ en Python y Streamlit | Proyecto en desarrollo")

def render():
    configpage()

    # --- Cabecera ---
    st.markdown("# 📊 Open Spain Insights")
    st.markdown("### Transparencia, acceso y análisis de datos públicos de España")
    st.markdown(INTRO_TEXT)

    st.markdown("---")

    # --- Sección ¿Por qué este proyecto? ---
    st.markdown("## ✨ ¿Por qué este proyecto?")
    st.markdown(
        """
        Los datos no son solo números. Son decisiones, historias y derechos.  
        Open Spain Insights nace del compromiso con una España más transparente y comprensible.
        """
    )

    # --- Transparencia y metodología ---
    with st.expander("📖 ¿Cómo trabajamos?"):
        st.markdown("""
        - Cada dataset tiene su fuente y notas metodológicas.
        - Nunca alteramos los datos originales.
        - Puedes ver el código y sugerir mejoras en [GitHub](https://github.com/LordLiberte/DataHubSpain).
        """)

    show_footer()