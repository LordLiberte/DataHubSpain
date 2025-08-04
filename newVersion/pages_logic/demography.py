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
            editor_data = st.session_state.get("demography_data_editor", {})
            st.write(f"DEBUG: Type of editor_data: {type(editor_data)}")
            st.write(f"DEBUG: Value of editor_data: {editor_data}")

            if isinstance(editor_data, pd.DataFrame):
                df_selected = editor_data
            elif isinstance(editor_data, dict) and "edited_rows" in editor_data:
                # Aquí puedes reconstruir un DataFrame a partir de las ediciones si quieres.
                df_selected = df.copy()
                for idx, changes in editor_data["edited_rows"].items():
                    for col, val in changes.items():
                        df_selected.at[int(idx), col] = val
            else:
                df_selected = df  # fallback

            # Aquí iría la lógica de selección si has habilitado selección en la tabla
            # Pero como no la has configurado, no existe `_selected`

            st.warning("⚠️ La selección de filas no está activada. Debes configurar la tabla para permitirla.")
