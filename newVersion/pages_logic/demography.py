import streamlit as st
import sys
import os

# Añadir el directorio raíz al path para resolver la importación de 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core import data_browser, data_loader, data_cleaning, data_plotter
import altair as alt

def render():
    st.title("👨‍👩‍👧‍👦 Demografía")

    df = None
    # Usar st.session_state para mantener el estado del dataframe entre reruns
    if 'demography_df' not in st.session_state:
        st.session_state['demography_df'] = None

    category_path = "data/demografia"
    datasets = data_browser.listar_subcarpetas(category_path)

    selected_dataset = st.selectbox(
        "Selecciona un dataset",
        datasets,
        index=None,
        placeholder="Selecciona un dataset para continuar..."
    )

    # Cargar datos solo si se selecciona un nuevo dataset
    if selected_dataset and st.session_state.get('demography_selected_dataset') != selected_dataset:
        dataset_path = os.path.join(category_path, selected_dataset)
        df, metadata = data_loader.load_dataset(dataset_path)
        st.session_state['demography_df'] = df
        st.session_state['demography_metadata'] = metadata
        st.session_state['demography_selected_dataset'] = selected_dataset
    
    # Asignar el dataframe desde el estado de la sesión
    df = st.session_state['demography_df']
    metadata = st.session_state.get('demography_metadata')

    if metadata:
        st.markdown(metadata)

    if st.button("Limpiar Datos"):
        if df is not None:
            # Actualizar el dataframe en el estado de la sesión
            st.session_state['demography_df'] = data_cleaning.delete_none(df)
            st.rerun() # Forzar un rerun para mostrar el df limpiado
        else:
            st.write("No hay datos para limpiar")

    if df is not None:
        st.markdown("### 👀 Vista interactiva del dataset")
        st.info("Selecciona filas en la tabla de abajo para generar una gráfica.")
        
        st.dataframe(
            df,
            on_select="rerun",
            selection_mode="multi-row",
            key="demography_selector"
        )

        if "demography_selector" in st.session_state:
            selected_rows_indices = st.session_state["demography_selector"]["selection"]["rows"]

            if selected_rows_indices:
                selected_df = df.iloc[selected_rows_indices]
                st.success(f"{len(selected_df)} fila(s) seleccionadas")

                st.markdown("### 📊 Gráfico generado automáticamente")
                chart = data_plotter.generate_dynamic_chart(selected_df)
                
                if chart:
                    st.altair_chart(chart, use_container_width=True)
                else:
                    st.warning("No se pudo generar un gráfico. Asegúrate de que los datos seleccionados contengan al menos una columna de texto/categoría y una columna numérica.")