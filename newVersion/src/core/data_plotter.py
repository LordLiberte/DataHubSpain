import altair as alt
import pandas as pd

def generate_dynamic_chart(df: pd.DataFrame):
    """
    Genera un gráfico de barras de Altair automáticamente desde un dataframe.

    Intenta identificar las mejores columnas para los ejes X, Y y el color:
    - Eje X: La primera columna categórica (object, category).
    - Eje Y: La primera columna numérica (int, float).
    - Color: La segunda columna categórica, si existe.
    
    Si no encuentra columnas adecuadas, devuelve None.
    """
    if df.empty:
        return None

    # Identificar tipos de columnas
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    if not numeric_cols or not categorical_cols:
        return None # No hay suficientes columnas para graficar

    # Asignar ejes
    x_axis = categorical_cols[0]
    y_axis = numeric_cols[0]
    
    # Usar una segunda columna categórica para el color si está disponible
    color_axis = None
    if len(categorical_cols) > 1:
        color_axis = categorical_cols[1]

    # Crear el gráfico
    try:
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X(f'{x_axis}:N', title=x_axis), # :N indica que es nominal (categórica)
            y=alt.Y(f'{y_axis}:Q', title=y_axis)  # :Q indica que es cuantitativa (numérica)
        ).properties(
            title=f'Gráfico de {y_axis} por {x_axis}',
            height=400
        )

        if color_axis:
            chart = chart.encode(color=alt.Color(f'{color_axis}:N', title=color_axis))
        
        return chart
    except Exception as e:
        # st.error(f"Error al generar el gráfico: {e}")
        return None
