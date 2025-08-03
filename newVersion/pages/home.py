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

    st.markdown("---")

    # --- Navegación rápida ---
    st.markdown("## 🔍 Explora por secciones")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📈 Economía", use_container_width=True):
            st.experimental_set_query_params(page="economy")
    with col2:
        if st.button("🧑‍🤝‍🧑 Población", use_container_width=True):
            st.experimental_set_query_params(page="population")
    with col3:
        if st.button("🚉 Transporte", use_container_width=True):
            st.experimental_set_query_params(page="transport")

    st.markdown("---")

    # --- Transparencia y metodología ---
    with st.expander("📖 ¿Cómo trabajamos?"):
        st.markdown("""
        - Cada dataset tiene su fuente y notas metodológicas.
        - Nunca alteramos los datos originales.
        - Puedes ver el código y sugerir mejoras en [GitHub](https://github.com/tu-repo).
        """)

    show_footer()