# ===========================================================================================
# Librerias
import streamlit as st
import pandas as pd
# ===========================================================================================


# ===========================================================================================
# Funciones y caracteristicas

def dataTest():
    df_ventas = pd.DataFrame({
        'Fecha': pd.date_range(start='2025-01-01', periods=10, freq='D'),
        'Producto': ['Camiseta', 'Pantalón', 'Zapatos', 'Chaqueta', 'Gorra',
                    'Camiseta', 'Zapatos', 'Pantalón', 'Gorra', 'Chaqueta'],
        'Categoría': ['Ropa', 'Ropa', 'Calzado', 'Ropa', 'Accesorios',
                    'Ropa', 'Calzado', 'Ropa', 'Accesorios', 'Ropa'],
        'Precio Unitario (€)': [20, 35, 60, 50, 15, 22, 65, 30, 17, 55],
        'Unidades Vendidas': [3, 2, 1, 4, 5, 2, 1, 3, 2, 1],
        })

    # Calcular ingreso total por fila
    df_ventas['Ingresos'] = df_ventas['Precio Unitario (€)'] * df_ventas['Unidades Vendidas']
    return df_ventas
        
def IniciarOpcion():
    """
    Inicia la opción seleccionada en la barra lateral.
    """
    
    st.markdown("# Spain Data Hub :bar_chart:")

    st.markdown("""
    ¡Bienvenido a **Spain Data Hub**! Tu portal interactivo para explorar y analizar datos de España. 
    Construido con Python y la potencia de Streamlit, este proyecto se basa en datos 
    reales y oficiales para ofrecerte una experiencia de visualización única.

    **¿Qué puedes hacer aquí?**
    * **Visualizar datos:** Explora gráficos y mapas interactivos.
    * **Analizar información:** Descubre tendencias y patrones ocultos.
    * **Interactuar con la app:** Usa una interfaz amigable e intuitiva.

    Todos los datos han sido procesados y limpiados para asegurar la máxima fiabilidad.
    
    Aquí puedes ver algunos ejemplos (datos inventados) que podrás encontrar en este proyecto:

    """)
    
    tabData, tabVis = st.tabs(["Datos", "Visualización"])
        
    with tabData:

        # Mostrar DataFrame (útil en Streamlit)
        st.table(dataTest())
    
    
    with tabVis:

        # Mostrar gráfico
        st.bar_chart(data=dataTest(), x='Categoría', y='Ingresos')
        
    
    
    st.markdown("## Conecta con nosotros :globe_with_meridians:")
    st.markdown("Sigue el proyecto y no te pierdas las novedades:")
    st.markdown("- **GitHub:** [LordLiberte](https://github.com/LordLiberte)")
    st.markdown("- **X:** [LordAivazovsky](https://x.com/LordAivazovsky)")
    st.markdown("- **Codeforces:** [CarlosGR01](https://codeforces.com/profile/CarlosGR01)")
    st.markdown("Si tienes alguna pregunta o sugerencia, no dudes en contactarme.")