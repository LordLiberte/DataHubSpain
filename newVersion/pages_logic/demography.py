import streamlit as st
import sys
import os

# Añadir el directorio raíz al path para resolver la importación de 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core import data_browser, data_loader, data_cleaning, data_plotter

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

    # Cargar datos solo si se selecciona un nuevo dataset
    if selected_dataset and st.session_state.demography_selected_dataset != selected_dataset:
        dataset_path = os.path.join(category_path, selected_dataset)
        df, metadata = data_loader.load_dataset(dataset_path)
        st.session_state.demography_df = df
        st.session_state.demography_metadata = metadata
        st.session_state.demography_selected_dataset = selected_dataset
        # Limpiar la selección de filas y columnas al cambiar de dataset
        st.session_state.demography_selector = {"selection": {"rows": []}}
        st.rerun()

    df = st.session_state.demography_df
    metadata = st.session_state.demography_metadata

    if metadata:
        st.markdown(metadata)

    if st.button("Limpiar Datos"):
        if df is not None:
            st.session_state.demography_df = data_cleaning.delete_none(df)
            st.rerun()
        else:
            st.warning("No hay datos para limpiar")

    if df is not None:
        st.markdown("### 👀 Vista interactiva del dataset")
        st.info("Selecciona filas en la tabla de abajo para generar una gráfica.")
        
        st.dataframe(
            df,
            on_select="rerun",
            selection_mode="multi-row",
            key="demography_selector"
        )

        selected_rows_indices = st.session_state.demography_selector["selection"]["rows"]

        if selected_rows_indices:
            selected_df = df.iloc[selected_rows_indices]
            st.success(f"{len(selected_df)} fila(s) seleccionadas")

            st.markdown("### ⚙️ Configura tu gráfico")
            
            # Opciones para los ejes
            column_options = selected_df.columns.tolist()
            categorical_options = selected_df.select_dtypes(include=['object', 'category']).columns.tolist()
            numeric_options = selected_df.select_dtypes(include=['number']).columns.tolist()

            col1, col2, col3 = st.columns(3)
            with col1:
                x_axis = st.selectbox("Eje X (Categorías)", categorical_options)
            with col2:
                y_axis = st.selectbox("Eje Y (Valores)", numeric_options)
            with col3:
                color_axis = st.selectbox("Color (Opcional)", ["None"] + categorical_options)

            if x_axis and y_axis:
                chart = data_plotter.generate_dynamic_chart(selected_df, x_axis, y_axis, color_axis)
                if chart:
                    st.altair_chart(chart, use_container_width=True)
                else:
                    st.warning("No se pudo generar el gráfico con las columnas seleccionadas.")
