import streamlit as st
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
        edited_df = st.data_editor(
            df,
            use_container_width=True,
            num_rows="dynamic",
            key="demography_data_editor"
        )

        # Mostrar gráfico si se han seleccionado menos filas que el total (selección manual)
        if not edited_df.empty and len(edited_df) < len(df):
            st.success(f"{len(edited_df)} fila(s) seleccionadas")

            # Intentar graficar columnas si existen
            columnas = df.columns

            if "Edad" in columnas and "Total" in columnas and "Sexo" in columnas:
                st.markdown("### 📊 Gráfico generado automáticamente")
                chart = altair_chart_from_selection(edited_df)
                st.altair_chart(chart, use_container_width=True)
            else:
                st.warning("No se encontraron columnas adecuadas para graficar (se esperan 'Edad', 'Total', 'Sexo').")
        else:
            st.info("Selecciona filas para ver una gráfica generada.")

def altair_chart_from_selection(df):
    import altair as alt
    chart = alt.Chart(df).mark_bar().encode(
        x="Edad:N",
        y="Total:Q",
        color="Sexo:N"
    ).properties(height=400)
    return chart

            
   