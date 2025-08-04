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

    if selected_dataset and st.session_state.demography_selected_dataset != selected_dataset:
        dataset_path = os.path.join(category_path, selected_dataset)
        df, metadata = data_loader.load_dataset(dataset_path)
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
            st.session_state.demography_df = data_cleaning.delete_none(df)
            st.rerun()
        else:
            st.warning("No hay datos para limpiar")

    if df is not None:
        st.markdown("### 👀 Vista interactiva del dataset")
        st.info("1. Selecciona las filas que quieres visualizar en la tabla de abajo.")

        # Mostramos el editor. Su estado se guarda en st.session_state.demography_data_editor
        st.data_editor(
            df,
            use_container_width=True,
            num_rows="dynamic",
            key="demography_data_editor"
        )

        st.info("2. Pulsa el botón para generar el gráfico con las filas seleccionadas.")
        if st.button("📊 Generar Gráfico con Selección"):
            # Accedemos al estado del editor directamente desde st.session_state
            edited_df_from_state = st.session_state["demography_data_editor"]

            if "_selected" in edited_df_from_state.columns and edited_df_from_state["_selected"].any():
                selected_df = edited_df_from_state[edited_df_from_state["_selected"] == True]
                st.success(f"{len(selected_df)} fila(s) seleccionadas.")

                st.markdown("### ⚙️ Configura tu gráfico")
                st.info("3. Elige las columnas para los ejes X e Y.")

                categorical_options = selected_df.select_dtypes(include=['object', 'category']).columns.tolist()
                numeric_options = selected_df.select_dtypes(include=['number']).columns.tolist()

                if not categorical_options or not numeric_options:
                    st.warning("Para generar un gráfico, la selección debe contener al menos una columna de texto/categorías y una columna numérica.")
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
                st.warning("No has seleccionado ninguna fila. Por favor, selecciona al menos una fila en la tabla de arriba.")