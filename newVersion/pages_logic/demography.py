import streamlit as st
import sys
import os

# Añadir el directorio raíz al path para resolver la importación de 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core import data_browser, data_loader, data_cleaning
import os
import altair as alt

def render():
    st.title("👨‍👩‍👧‍👦 Demografía")

    df = None
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
            st.write("No hay datos para limpiar")

    if df is not None:
        st.markdown("### 👀 Vista interactiva del dataset")
        st.info("Selecciona filas en la tabla de abajo para generar una gráfica.")
        
        # Usar st.dataframe con on_select para capturar las selecciones de filas
        st.dataframe(
            df,
            on_select="rerun",
            selection_mode="multi-row",
            key="demography_selector"
        )

        # Recuperar la selección del estado de la sesión
        if "demography_selector" in st.session_state:
            selected_rows_indices = st.session_state["demography_selector"]["selection"]["rows"]

            if selected_rows_indices:
                # Crear un dataframe solo con las filas seleccionadas
                selected_df = df.iloc[selected_rows_indices]
                st.success(f"{len(selected_df)} fila(s) seleccionadas")

                # Comprobar las columnas necesarias y generar el gráfico
                columnas = selected_df.columns
                if "Edad" in columnas and "Total" in columnas and "Sexo" in columnas:
                    st.markdown("### 📊 Gráfico generado automáticamente")
                    chart = altair_chart_from_selection(selected_df)
                    st.altair_chart(chart, use_container_width=True)
                else:
                    st.warning("Las filas seleccionadas no tienen las columnas adecuadas para graficar (se esperan 'Edad', 'Total', 'Sexo').")

def altair_chart_from_selection(df):
    import altair as alt
    chart = alt.Chart(df).mark_bar().encode(
        x="Edad:N",
        y="Total:Q",
        color="Sexo:N"
    ).properties(height=400)
    return chart

            
   