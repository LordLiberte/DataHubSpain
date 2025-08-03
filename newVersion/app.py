# Librerias y módulos
import streamlit as st
from src.components.sidebar import create_sidebar
from pages import economy, home


# Función principal para el render de la web
def main():
    
    # Barra lateral
    pagina = create_sidebar()
    
    # Selección de sidebar
    if pagina == "home":
        home.render()
        
    elif pagina == "economy":
        economy.render()

    
# ==============================================================
if __name__ == "__main__":
    main()