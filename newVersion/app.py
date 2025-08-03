# Librerias
import streamlit as st
from src.config.constants import INTRO_TEXT


# Funciones para el funcionamiento del programa
def configpage():
    # Configuración general de la app
    st.set_page_config(
        page_title="Open Spain Insights",
        page_icon="🇪🇸",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
def show_footer():
    # Footer
    st.markdown("---")
    st.caption("Hecho con ❤️ en Python y Streamlit | Proyecto en desarrollo")



# Función principal para el render de la web
def main():
    
    # Configuración general de la app
    configpage()
    
    # Cabecera
    st.title("📊 Open Spain Insights")
    st.subheader("Transparencia, acceso y análisis de datos públicos de España")

    st.markdown(INTRO_TEXT)

    # Footer
    st.markdown("---")
    st.caption("Hecho con ❤️ en Python y Streamlit | Proyecto en desarrollo")
    

if __name__ == "__main__":
    main()