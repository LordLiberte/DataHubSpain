import streamlit as st
import pandas as pd
from funciones import data_frames
import os


def main(dataset=None):
    st.title("Datos")

    if dataset == "demografia":
        st.subheader("Datos de Población por Fecha, Sexo y Edad")
        # Ir al directorio raíz del proyecto (subir dos niveles desde este archivo)
        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        ruta = os.path.join(BASE_DIR, "data", "Demografia", "PoblacionResFechaSexoEdad.xlsx")
        
        st.write(ruta)

        try:
            df = pd.read_excel(ruta)
            df = data_frames.limpiezaData(df)
            st.dataframe(df)
            st.markdown("*Fuente*: Instituto Nacional de Estadistica, INE")
            st.markdown("A través de Data Hub")
        except FileNotFoundError:
            st.error("No se encontró el archivo de datos. Contacta con el administrador.")
        except Exception:
            st.error("Ocurrió un error al cargar los datos. Inténtalo de nuevo más tarde o contacta con el administrador.")

    elif dataset:
        st.warning(f"No se reconoce el dataset '{dataset}'. Contacta con el administrador")
    else:
        st.info("Selecciona un dataset para mostrar sus datos.")