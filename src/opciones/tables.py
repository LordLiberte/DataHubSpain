import os
import pandas as pd
import streamlit as st
from funciones import data_frames

def main(dataset=None):
    st.title("Datos")

    if dataset == "demografia":
        st.subheader("Datos de Población por Fecha, Sexo y Edad")

        # Ruta absoluta basada en la estructura real del proyecto
        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        ruta = os.path.join(BASE_DIR, "data", "Demografia", "PoblacionResFechaSexoEdad.xlsx")

        try:
            df = pd.read_excel(ruta, engine="openpyxl")
            df = data_frames.limpiezaData(df)
            st.dataframe(df)
            st.markdown("*Fuente*: Instituto Nacional de Estadistica, INE")
            st.markdown("A través de Data Hub")
        except FileNotFoundError:
            st.error(f"No se encontró el archivo de datos en la ruta:\n\n`{ruta}`")
        except Exception as e:
            st.error(f"Ocurrió un error al cargar los datos: {e}")