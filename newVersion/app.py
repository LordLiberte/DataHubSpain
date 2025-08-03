# Librerias y módulos
import streamlit as st
import base64
import os
from src.components.sidebar import create_sidebar
from src.config.routing import ROUTES

# Configuración de la página
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "icons", "base-de-datos.ico")

with open(icon_path, "rb") as f:
    icon_b64 = base64.b64encode(f.read()).decode("utf-8")

st.set_page_config(
    page_title="Open Spain Insights",
    page_icon=f"data:image/x-icon;base64,{icon_b64}",
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