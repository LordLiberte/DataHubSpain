# Librerias y módulos
import streamlit as st
import base64
import os
import sys

# Añadir el directorio raíz al path de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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

from pages.home import render as home_render

# Función principal para el render de la web
def main():
    
    # Render de la página principal
    home_render()
    
# ==============================================================
if __name__ == "__main__":
    main()