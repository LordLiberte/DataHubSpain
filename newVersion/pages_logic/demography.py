import streamlit as st
from src.core import data_browser, data_loader
import os
from src.core import data_cleaning

# Funciones para el funcionamiento de la página



# Función principal 
def render():
    st.title("👨‍👩‍👧‍👦 Demografía")
    
    df = None;
    category_path = "data/demografia"
    datasets = data_browser.listar_subcarpetas(category_path)
    
    selected_dataset = st.selectbox(
        "Selecciona un dataset",
        datasets,
        index=None,
        placeholder="Selecciona un dataset para continuar..."
    )
    
    if selected_dataset:
        dataset_path = os.path.join(category_path, selected_dataset)
        df, metadata = data_loader.load_dataset(dataset_path)
        
        if metadata:
            st.markdown(metadata)
    
    if st.button("Limpiar Datos"):
        if df is not None:
            df = data_cleaning.delete_none(df)
        else:
            st.warning("No hay datos para limpiar")
            
    if df is not None:
        st.dataframe(df)
            
   