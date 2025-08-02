import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from opciones import acercade, tables, actualizaciones
from funciones import data_frames
    
def sideBar():
    
    # Titulo 
    st.sidebar.markdown("# Navegación :mag_right:")
    
    if st.sidebar.button("Actualizaciones", use_container_width=True):
        st.query_params.clear()
        st.query_params["page"] = ["actualizaciones"]
    
    # Boton de Consulta de Datos
    if st.sidebar.button("Consulta de Datos", use_container_width=True):
        st.query_params.clear()
        st.query_params["page"] = ["datos"]
        
    # Boton de Acerca De
    if st.sidebar.button("Acerca de", use_container_width=True):
        st.query_params.clear()
        st.query_params["page"] = ["acercade"]

# Este es el archivo principal de la aplicación Streamlit. Aquí se define la estructura y funcionalidad de la app
def main():
    
    st.set_page_config(
        page_title="Spain Data Hub",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    sideBar()
    params = st.query_params
    page = params.get("page", "actualizaciones")

    if page == "actualizaciones":
        actualizaciones.main()
    elif page == "datos":
        dataset = params.get("dataset", None)
        tables.main(dataset=dataset)
    else:
        acercade.IniciarOpcion()

    

if __name__ == "__main__":
    main()