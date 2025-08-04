import streamlit as st
import sys
import os

# Añadir el directorio raíz al path para resolver la importación de 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core import data_browser, data_loader

def render():
    st.title("👨‍👩‍👧‍👦 Demografía")

    # Usar st.session_state para mantener el estado entre reruns
    if 'demography_df' not in st.session_state:
        st.session_state.demography_df = None
        st.session_state.demography_metadata = None
        st.session_state.demography_selected_dataset = None

    category_path = "data/demografia"
    datasets = data_browser.listar_subcarpetas(category_path)

    selected_dataset = st.selectbox(
        "Selecciona un dataset",
        datasets,
        index=None,
        placeholder="Selecciona un dataset para continuar...",
        key="demography_dataset_selector"
    )

    # Cargar datos solo si se selecciona un nuevo dataset o si no hay df cargado
    if selected_dataset and (st.session_state.demography_selected_dataset != selected_dataset or st.session_state.demography_df is None):
        dataset_path = os.path.join(category_path, selected_dataset)
        df, metadata = data_loader.load_dataset(dataset_path)
        st.session_state.demography_df = df
        st.session_state.demography_metadata = metadata
        st.session_state.demography_selected_dataset = selected_dataset
        # Reset data_editor state when a new dataset is loaded
        if "demography_data_editor" in st.session_state:
            del st.session_state["demography_data_editor"]
        st.rerun()

    df = st.session_state.demography_df
    metadata = st.session_state.demography_metadata

    if metadata:
        st.markdown(metadata)

    if df is not None:
        st.markdown("### 👀 Vista interactiva del dataset")
        
        # Display the data editor without selection checkboxes for charting
        st.data_editor(
            df, # Use the original df, no need for _selected column
            use_container_width=True,
            num_rows="dynamic",
            key="demography_data_editor",
            disabled=df.columns.tolist() # Keep columns disabled for editing
        )
        
        # Display basic dataset information
        st.markdown("### 📊 Información del Dataset")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total de filas", len(df))
        with col2:
            st.metric("Total de columnas", len(df.columns))
