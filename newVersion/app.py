# Librerias
import streamlit as st
from src.config.constants import INTRO_TEXT
from src.components.sidebar import create_sidebar



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
    
    # Barra lateral
    pagina = create_sidebar()
    # Selección de sidebar
    if pagina == "home":
        st.title("📊 Open Spain Insights")
        st.subheader("Transparencia, acceso y análisis de datos públicos de España")
        st.markdown("Bienvenido a la página de inicio. Aquí empezarás tu viaje.")
        
    elif pagina == "economy":
        st.title("📈 Economía")
        st.write("Aquí irán los datos económicos.")
    
    """
    # Cabecera
    st.title("📊 Open Spain Insights")
    st.subheader("Transparencia, acceso y análisis de datos públicos de España")

    st.markdown(INTRO_TEXT)

    # Footer
    show_footer()
    """
    

if __name__ == "__main__":
    main()