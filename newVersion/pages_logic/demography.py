import streamlit as st
from src.core import data_browser, data_loader
import os


# Funciones para el funcionamiento de la página

# Función principal 
def render():
    st.title("👨‍👩‍👧‍👦 Demografía")
    st.write("Aquí irá la visualización de datos demograficos.")
    
    category_path = "data/demografia"
    datasets = data_browser.listar_subcarpetas(category_path)
    st.write(datasets)
    
    selected_dataset = st.selectbox("Selecciona un dataset", datasets)
    
    if selected_dataset:
        dataset_path = os.path.join(category_path, selected_dataset)
        df, metadata = data_loader.load_dataset(dataset_path)
        
        st.markdown(f"### 📁 {selected_dataset}")
        if metadata:
            st.markdown(metadata)
        st.dataframe(df)