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
        [cite_start]democratizando el acceso y la visibilidad de la información[cite: 197].
        Nuestro valor no es solo por la presencia de los datos, sino por la autonomía y el poder que permitimos
        [cite_start]a las masas que buscan saciar su sed de datos y conocer el mundo que les rodea[cite: 205].
        """
    )
    
    st.markdown("---")

    # --- Principios del proyecto ---
    with st.expander("💖 ¿Qué nos diferencia?"):
        st.markdown(
            """
            [cite_start]Lo que nos diferencia es nuestro amor por el dato [cite: 200][cite_start], y nuestro afán de ser transparentes, éticos y estrictos en el cumplimiento de estos valores[cite: 201].
            [cite_start]Buscamos crear visualizaciones que marquen la diferencia, que a simple vista se sepa de qué se está hablando[cite: 203].
            [cite_start]Nos diferenciamos en querer dar una gran independencia al usuario [cite: 202][cite_start], facilitando al mismo instante a aquellos inexpertos del tema[cite: 202].
            [cite_start]Buscamos transparencia y facilitar el acceso a las fuentes originales junto a su metodología[cite: 204].
            """
        )

    # --- Objetivos ---
    with st.expander("🎯 ¿Cuáles son nuestros objetivos?"):
        st.markdown(
            """
            ### A corto plazo (versión inicial)
            * [cite_start]Empezar mostrando tablas y visualizaciones ya creadas, por el momento de forma rígida[cite: 213, 215].
            * [cite_start]El objetivo es tener una base funcional desde el principio y crear un catálogo de visualizaciones útiles que luego podrán evolucionar[cite: 218, 222].

            ### A medio y largo plazo
            * [cite_start]Introducir funcionalidades como herramientas para cruzar datasets y limpieza de datos[cite: 228, 229].
            * [cite_start]Permitir la creación de nuevas visualizaciones personalizadas con distintos tipos de gráficos y filtros[cite: 230].
            * [cite_start]Aspiramos a ampliar el alcance con inteligencia artificial, predicciones y análisis automatizados[cite: 233, 234, 235].
            * [cite_start]Explorar una comunidad colaborativa[cite: 237].
            """
        )

    # --- Características de la versión mínima viable (MVV) ---
    with st.expander("🚀 ¿Qué podrás hacer en la versión inicial?"):
        st.markdown(
            """
            En su versión inicial, la aplicación te permitirá:
            * [cite_start]Consultar datos y visualizaciones ya creadas, categorizadas por tema o sector[cite: 240].
            * [cite_start]Explorar tablas y gráficos con una estructura clara y accesible[cite: 241].
            * [cite_start]Descargar las tablas en formatos útiles como `.csv`, `.xlsx` o `.json`[cite: 242].
            * [cite_start]Descargar las visualizaciones como imagen para usar en presentaciones[cite: 243].
            * [cite_start]Acceder a la fuente original del dataset, con enlaces directos[cite: 246].
            * [cite_start]Consultar la metodología asociada a cada conjunto de datos[cite: 247].
            """
        )

    # --- Datos iniciales ---
    with st.expander("📋 ¿Qué tipo de datos vamos a incluir?"):
        st.markdown(
            """
            [cite_start]Los datos iniciales se basarán en fuentes oficiales y fiables [cite: 260][cite_start], como el Instituto Nacional de Estadística (INE) [cite: 261][cite_start], ministerios (Igualdad, Interior, Transportes) [cite: 263, 264, 265][cite_start], Seguridad Social [cite: 266] [cite_start]y repositorios públicos de datos abiertos de la Administración General del Estado[cite: 271].

            Las temáticas principales abordadas serán:
            * [cite_start]Economía [cite: 273]
            * [cite_start]Transporte [cite: 274]
            * [cite_start]Bienestar social [cite: 275]
            * [cite_start]Seguridad [cite: 276]
            * [cite_start]Flujos migratorios [cite: 277]
            * [cite_start]Mercado laboral [cite: 278]
            * [cite_start]Población y demografía [cite: 279]
            * [cite_start]Vivienda y entorno urbano [cite: 280]
            """
        )

    # --- Colaboración ---
    with st.expander("🤝 ¿Quieres colaborar?"):
        st.markdown(
            """
            [cite_start]Este proyecto nace con vocación comunitaria, así que hay varias formas de sumar[cite: 359]:
            * [cite_start]**Apoyar económicamente:** Si quieres ayudar al mantenimiento y desarrollo del proyecto, puedes hacer una aportación puntual a través de PayPal (próximamente disponible)[cite: 361].
            * **Aportar ideas y sugerencias:** ¿Has visto un dataset interesante o se te ocurre una nueva funcionalidad? [cite_start]¡Queremos escucharte![cite: 365].
            * [cite_start]**Unirte al proyecto:** Si te apasiona la transparencia y la inteligencia pública, puedes formar parte del equipo[cite: 367].
            """
        )

    st.markdown("---")

    # --- Sección ¿Cómo trabajamos? (Manteniendo el expander original) ---
    with st.expander("📖 ¿Cómo trabajamos?"):
        st.markdown("""
        - [cite_start]Cada dataset tiene su fuente y notas metodológicas[cite: 247, 287, 290, 299].
        - [cite_start]Nunca alteramos los datos originales[cite: 297].
        - Puedes ver el código y sugerir mejoras en [GitHub](https://github.com/LordLiberte/DataHubSpain).
        """)

    # Llama a tu función de pie de página, si existe
    show_footer()