# Librerias y módulos
import streamlit as st
from src.components.sidebar import create_sidebar
from src.config.routing import ROUTES

# Configuración de la página
st.set_page_config(
    page_title="Open Spain Insights",
    page_icon="icons/base-de-datos.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Función principal para el render de la web
def main():
    
    # Barra lateral
    pagina = create_sidebar()
    
    # Selección de sidebar
    for key, _, module in ROUTES:
        if key == pagina:
            module.render()
            break  # Ya encontramos la página, salimos del bucle
    

    
# ==============================================================
if __name__ == "__main__":
    main()