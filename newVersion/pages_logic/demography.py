import streamlit as st
import sys
import os
import pandas as pd

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

    if selected_dataset and st.session_state.demography_selected_dataset != selected_dataset:
        dataset_path = os.path.join(category_path, selected_dataset)
        df, metadata = data_loader.load_dataset(dataset_path)

        # Añadir columna '_selected' al cargar el dataset
        if "_selected" not in df.columns:
            df["_selected"] = False

        st.session_state.demography_df = df
        st.session_state.demography_metadata = metadata
        st.session_state.demography_selected_dataset = selected_dataset
        st.rerun()

    df = st.session_state.demography_df
    metadata = st.session_state.demography_metadata

    if metadata:
        st.markdown(metadata)

    if st.button("Limpiar Datos"):
        if df is not None:
            cleaned_df = data_cleaning.delete_none(df)

            # Asegurar que se conserva la columna de selección
            if "_selected" not in cleaned_df.columns:
                cleaned_df["_selected"] = False

            st.session_state.demography_df = cleaned_df
            st.rerun()
        else:
            st.warning("No hay datos para limpiar")

    if df is not None:
        st.markdown("### 👀 Vista interactiva del dataset")
        st.info("1. Marca las filas que quieres seleccionar para el gráfico.")

        # Mostrar el editor con columna de selección
        edited_df = st.data_editor(
            df,
            use_container_width=True,
            num_rows="dynamic",
            key="demography_data_editor"
        )

        st.info("2. Pulsa el botón para generar el gráfico con las filas seleccionadas.")

        if st.button("📊 Generar Gráfico con Selección"):
            st.write(f"DEBUG: Type of edited_df: {type(edited_df)}")
            st.write(f"DEBUG: Value of edited_df: {edited_df}")

            if isinstance(edited_df, pd.DataFrame) and "_selected" in edited_df.columns:
                selected_df = edited_df[edited_df["_selected"] == True]

                if not selected_df.empty:
                    st.success(f"{len(selected_df)} fila(s) seleccionadas.")

                    st.markdown("### ⚙️ Configura tu gráfico")
                    st.info("3. Elige las columnas para los ejes X e Y.")

                    categorical_options = selected_df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()
                    numeric_options = selected_df.select_dtypes(include=['number']).columns.tolist()

                    if not categorical_options or not numeric_options:
                        st.warning("La selección debe contener al menos una columna categórica y una numérica.")
                        return

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        x_axis = st.selectbox("Eje X (Categorías)", categorical_options, key="x_axis_selector")
                    with col2:
                        y_axis = st.selectbox("Eje Y (Valores)", numeric_options, key="y_axis_selector")
                    with col3:
                        color_axis = st.selectbox("Color (Opcional)", ["None"] + categorical_options, key="color_axis_selector")

                    if x_axis and y_axis:
                        chart = data_plotter.generate_dynamic_chart(selected_df, x_axis, y_axis, color_axis)
                        if chart:
                            st.altair_chart(chart, use_container_width=True)
                        else:
                            st.error("No se pudo generar el gráfico con las columnas seleccionadas.")
                else:
                    st.warning("No has seleccionado ninguna fila. Marca al menos una con el checkbox.")
            else:
                st.error("Error: No se pudo obtener la selección. Revisa el estado del editor.")
