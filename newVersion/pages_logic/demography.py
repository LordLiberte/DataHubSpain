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
        # CORRECCIÓN 1: Llamar correctamente a la función load_dataset
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

        # CORRECCIÓN 2: Añadir columna de selección si no existe
        df_with_selection = df.copy()
        if "_selected" not in df_with_selection.columns:
            df_with_selection.insert(0, "_selected", False)

        # st.data_editor returns the (potentially edited) dataframe
        # The key stores the *current* state of the editor in session_state
        edited_df = st.data_editor(
            df_with_selection,
            use_container_width=True,
            num_rows="dynamic",
            key="demography_data_editor",
            column_config={
                "_selected": st.column_config.CheckboxColumn(
                    "Seleccionar",
                    help="Selecciona las filas para incluir en el gráfico",
                    default=False,
                )
            },
            disabled=df.columns.tolist()  # Deshabilitar edición de columnas de datos originales
        )

        st.info("2. Pulsa el botón para generar el gráfico con las filas seleccionadas.")
        if st.button("📊 Generar Gráfico con Selección"):
            # CORRECCIÓN 3: Usar directamente el dataframe editado devuelto por st.data_editor
            current_edited_df = edited_df
            
            if "_selected" in current_edited_df.columns and current_edited_df["_selected"].any():
                # CORRECCIÓN 4: Filtrar correctamente las filas seleccionadas
                selected_df = current_edited_df[current_edited_df["_selected"] == True].copy()
                # Remover la columna de selección del dataframe para el gráfico
                selected_df = selected_df.drop(columns=["_selected"])
                
                st.success(f"{len(selected_df)} fila(s) seleccionadas.")

                st.markdown("### ⚙️ Configura tu gráfico")
                st.info("3. Elige las columnas para los ejes X e Y.")

                # CORRECCIÓN 5: Mejorar la detección de tipos de columnas
                categorical_options = selected_df.select_dtypes(include=['object', 'category', 'string']).columns.tolist()
                numeric_options = selected_df.select_dtypes(include=['number', 'int64', 'float64']).columns.tolist()

                # CORRECCIÓN 6: Permitir columnas numéricas también en el eje X
                all_columns = selected_df.columns.tolist()

                if len(all_columns) < 2:
                    st.warning("Para generar un gráfico, la selección debe contener al menos dos columnas.")
                    return

                col1, col2, col3 = st.columns(3)
                with col1:
                    x_axis = st.selectbox("Eje X", all_columns, key="x_axis_selector")
                with col2:
                    y_axis = st.selectbox("Eje Y (Preferiblemente numérico)", all_columns, key="y_axis_selector")
                with col3:
                    color_options = ["None"] + categorical_options
                    color_axis = st.selectbox("Color (Opcional)", color_options, key="color_axis_selector")

                if x_axis and y_axis and x_axis != y_axis:
                    # CORRECCIÓN 7: Manejar el caso cuando color_axis es "None"
                    color_col = None if color_axis == "None" else color_axis
                    
                    try:
                        chart = data_plotter.generate_dynamic_chart(selected_df, x_axis, y_axis, color_col)
                        if chart:
                            st.altair_chart(chart, use_container_width=True)
                        else:
                            st.error("No se pudo generar el gráfico con las columnas seleccionadas.")
                    except Exception as e:
                        st.error(f"Error al generar el gráfico: {str(e)}")
                        st.info("Verifica que las columnas seleccionadas sean compatibles para la visualización.")
                elif x_axis == y_axis:
                    st.warning("Los ejes X e Y deben ser diferentes.")
            else:
                st.warning("No has seleccionado ninguna fila. Por favor, selecciona al menos una fila marcando las casillas en la columna 'Seleccionar'.")
        
        # CORRECCIÓN 8: Mostrar información adicional sobre el dataset
        st.markdown("### 📊 Información del Dataset")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de filas", len(df))
        with col2:
            st.metric("Total de columnas", len(df.columns))
        with col3:
            if "_selected" in edited_df.columns:
                selected_count = edited_df["_selected"].sum()
                st.metric("Filas seleccionadas", selected_count)