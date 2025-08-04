import streamlit as st
from src.core import data_browser, data_loader
import os


# Funciones para el funcionamiento de la página

# Función principal 
def render():
    st.title("👨‍👩‍👧‍👦 Demografía")
    
    category_path = "data/demografia"
    datasets = data_browser.listar_subcarpetas(category_path)
    
    # Añadir una opción vacía al principio
    datasets.insert(0, "")
    
    # El usuario selecciona el dataset que quiere
    selected_dataset = st.selectbox("Selecciona un dataset", datasets)
    
    if selected_dataset:
        dataset_path = os.path.join(category_path, selected_dataset)
        df, metadata = data_loader.load_dataset(dataset_path)
        
        if metadata:
            st.markdown(metadata)
        st.dataframe(df)