import streamlit as st

def main():
    
    st.markdown("# Últimas Actualizaciones")

    col1, col2, col3 = st.columns(3)

    with col1.expander("Demografía"):
        st.markdown("""
        Se han añadido datos sobre la altura de las personas en España por sexo, edad y número de personas por rango de altura. Los datos presentes 
        son del Instituto Nacional de Estadística.

        - Fuente oficial:
        """)
        st.link_button("Fuente INE", url="https://ine.es/jaxi/Tabla.htm?path=/t25/p442/histo/a1999/&file=02082.px&L=0", use_container_width=True)

        st.markdown("- Ver en la app con los datos cargados:")

        st.link_button("Ver datos", url="/?page=datos&dataset=demografia", use_container_width=True)


    