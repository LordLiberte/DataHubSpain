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

        # CORRECCIÓN: Mantener el estado de configuración del gráfico
        # Inicializar variables de estado para la configuración del gráfico
        if 'demography_show_config' not in st.session_state:
            st.session_state.demography_show_config = False
        if 'demography_selected_df' not in st.session_state:
            st.session_state.demography_selected_df = None

        st.info("2. Pulsa el botón para configurar el gráfico con las filas seleccionadas.")
        
        # Verificar si hay filas seleccionadas
        current_edited_df = edited_df
        has_selection = "_selected" in current_edited_df.columns and current_edited_df["_selected"].any()
        
        if st.button("📊 Configurar Gráfico con Selección") and has_selection:
            # Filtrar y guardar las filas seleccionadas en el estado
            selected_df = current_edited_df[current_edited_df["_selected"] == True].copy()
            selected_df = selected_df.drop(columns=["_selected"])
            st.session_state.demography_selected_df = selected_df
            st.session_state.demography_show_config = True
            st.rerun()

        # Mostrar la configuración del gráfico si está activada
        if st.session_state.demography_show_config and st.session_state.demography_selected_df is not None:
            selected_df = st.session_state.demography_selected_df
            st.success(f"{len(selected_df)} fila(s) seleccionadas para el gráfico.")

            st.markdown("### ⚙️ Configura tu gráfico")
            st.info("3. Elige las columnas para los ejes X e Y, luego genera el gráfico.")

            # CORRECCIÓN 5: Mejorar la detección de tipos de columnas
            categorical_options = selected_df.select_dtypes(include=['object', 'category', 'string']).columns.tolist()
            numeric_options = selected_df.select_dtypes(include=['number', 'int64', 'float64']).columns.tolist()
            all_columns = selected_df.columns.tolist()

            if len(all_columns) < 2:
                st.warning("Para generar un gráfico, la selección debe contener al menos dos columnas.")
                st.session_state.demography_show_config = False
                return

            # Configuración de ejes que persiste entre re-runs
            col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
            
            with col1:
                x_axis = st.selectbox(
                    "Eje X", 
                    all_columns, 
                    key="demography_x_axis_selector",
                    index=0
                )
            
            with col2:
                # Filtrar opciones para Y excluyendo la selección de X
                y_options = [col for col in all_columns if col != x_axis]
                y_axis = st.selectbox(
                    "Eje Y", 
                    y_options, 
                    key="demography_y_axis_selector",
                    index=0 if y_options else None
                )
            
            with col3:
                color_options = ["None"] + categorical_options
                color_axis = st.selectbox(
                    "Color (Opcional)", 
                    color_options, 
                    key="demography_color_axis_selector"
                )
            
            with col4:
                st.markdown("<br>", unsafe_allow_html=True)  # Espaciado
                if st.button("🎨 Generar", type="primary"):
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
                    else:
                        st.warning("Selecciona ejes X e Y diferentes para generar el gráfico.")

            # Botón para cerrar la configuración
            if st.button("❌ Cerrar Configuración"):
                st.session_state.demography_show_config = False
                st.session_state.demography_selected_df = None
                st.rerun()

        elif st.session_state.demography_show_config and not has_selection:
            st.warning("La selección de filas ha cambiado. Por favor, selecciona filas nuevamente.")
            st.session_state.demography_show_config = False
            st.session_state.demography_selected_df = None
        
        elif not has_selection and st.button("📊 Configurar Gráfico con Selección"):
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