# Librerias
import streamlit as st

# Configuración general de la app
st.set_page_config(
    page_title="Open Spain Insights",
    page_icon="🇪🇸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cabecera
st.title("📊 Open Spain Insights")
st.subheader("Transparencia, acceso y análisis de datos públicos de España")

st.markdown("""
Bienvenido a **Open Spain Insights**, tu plataforma para explorar y visualizar datos abiertos de España de manera clara, ética y accesible.

👉 Usa el menú lateral para acceder a las distintas secciones temáticas (economía, población, transporte, etc.)  
👉 Cada dataset viene acompañado de sus notas metodológicas y fuente oficial.

*Esto es solo el comienzo. Pronto podrás personalizar, cruzar y analizar los datos a tu medida.*  
""")

# Footer
st.markdown("---")
st.caption("Hecho con ❤️ en Python y Streamlit | Proyecto en desarrollo")