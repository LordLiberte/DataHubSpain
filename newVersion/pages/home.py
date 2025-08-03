import streamlit as st
from src.config.constants import INTRO_TEXT

def configpage():
    st.set_page_config(
        page_title="Open Spain Insights",
        page_icon="🇪🇸",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def show_footer():
    st.markdown("---")
    st.caption("Hecho con ❤️ en Python y Streamlit | Proyecto en desarrollo")

def render():
    
    # Llama a tu función de configuración
    configpage()

    # --- Cabecera ---
    st.markdown("# 📊 Open Spain Insights")
    st.markdown("### Transparencia, acceso y análisis de datos públicos de España")
    st.markdown(INTRO_TEXT)

    st.markdown("---")

    # --- Sección ¿Por qué este proyecto? ---
    st.markdown("## ¿Por qué este proyecto?")
    st.markdown(
        """
        Open Spain Insights nace del compromiso con una España más transparente y comprensible,
        democratizando el acceso y la visibilidad de la información.
        Nuestro valor no es solo por la presencia de los datos, sino por la autonomía y el poder que permitimos
        a las masas que buscan saciar su sed de datos y conocer el mundo que les rodea.
        """
    )
    
    st.markdown("---")

    # --- Principios del proyecto ---
    with st.expander("💖 ¿Qué nos diferencia?"):
        st.markdown(
            """
            Lo que nos diferencia es nuestro amor por el dato, y nuestro afán de ser transparentes, éticos y estrictos en el cumplimiento de estos valores.
            Buscamos crear visualizaciones que marquen la diferencia, que a simple vista se sepa de qué se está hablando.
            Nos diferenciamos en querer dar una gran independencia al usuario, facilitando al mismo instante a aquellos inexpertos del tema.
            Buscamos transparencia y facilitar el acceso a las fuentes originales junto a su metodología.
            """
        )

    # --- Objetivos ---
    with st.expander("🎯 ¿Cuáles son nuestros objetivos?"):
        st.markdown(
            """
            ### A corto plazo (versión inicial)
            * Empezar mostrando tablas y visualizaciones ya creadas, por el momento de forma rígida.
            * El objetivo es tener una base funcional desde el principio y crear un catálogo de visualizaciones útiles que luego podrán evolucionar.

            ### A medio y largo plazo
            * Introducir funcionalidades como herramientas para cruzar datasets y limpieza de datos.
            * Permitir la creación de nuevas visualizaciones personalizadas con distintos tipos de gráficos y filtros.
            * Aspiramos a ampliar el alcance con inteligencia artificial, predicciones y análisis automatizados.
            * Explorar una comunidad colaborativa.
            """
        )

    # --- Características de la versión mínima viable (MVV) ---
    with st.expander("🚀 ¿Qué podrás hacer en la versión inicial?"):
        st.markdown(
            """
            En su versión inicial, la aplicación te permitirá:
            * Consultar datos y visualizaciones ya creadas, categorizadas por tema o sector.
            * Explorar tablas y gráficos con una estructura clara y accesible.
            * Descargar las tablas en formatos útiles como `.csv`, `.xlsx` o `.json`.
            * Descargar las visualizaciones como imagen para usar en presentaciones.
            * Acceder a la fuente original del dataset, con enlaces directos.
            * Consultar la metodología asociada a cada conjunto de datos.
            """
        )

    # --- Datos iniciales ---
    with st.expander("📋 ¿Qué tipo de datos vamos a incluir?"):
        st.markdown(
            """
            Los datos iniciales se basarán en fuentes oficiales y fiables, como el Instituto Nacional de Estadística (INE), ministerios (Igualdad, Interior, Transportes), Seguridad Social y repositorios públicos de datos abiertos de la Administración General del Estado.

            Las temáticas principales abordadas serán:
            * Economía
            * Transporte
            """)
        

    # --- Colaboración ---
    with st.expander("🤝 ¿Quieres colaborar?"):
        st.markdown(
            """
            Este proyecto nace con vocación comunitaria, así que hay varias formas de sumar:
            ***Apoyar económicamente:** Si quieres ayudar al mantenimiento y desarrollo del proyecto, puedes hacer una aportación puntual a través de PayPal (próximamente disponible).
            ***Aportar ideas y sugerencias:** ¿Has visto un dataset interesante o se te ocurre una nueva funcionalidad? ¡Queremos escucharte!.
            ***Unirte al proyecto:** Si te apasiona la transparencia y la inteligencia pública, puedes formar parte del equipo.
            """
        )

    # --- ¿Cómo trabajamos?  ---
    with st.expander("📖 ¿Cómo trabajamos?"):
        st.markdown("""
        - Cada dataset tiene su fuente y notas metodológicas.
        - Nunca alteramos los datos originales.
        - Puedes ver el código y sugerir mejoras en [GitHub](https://github.com/LordLiberte/DataHubSpain).
        """)

    # Llama a tu función de pie de página
    show_footer()