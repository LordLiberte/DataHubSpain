import altair as alt
import pandas as pd

def generate_dynamic_chart(df: pd.DataFrame, x_axis: str, y_axis: str, color_axis: str = None):
    """
    Genera un gráfico de barras de Altair desde un dataframe usando las columnas especificadas.

    Args:
        df: El dataframe con los datos.
        x_axis: El nombre de la columna para el eje X.
        y_axis: El nombre de la columna para el eje Y.
        color_axis: (Opcional) El nombre de la columna para la codificación por color.
    """
    if df.empty or not x_axis or not y_axis:
        return None

    try:
        # Determinar el tipo de dato para el encoding de Altair
        x_type = 'N' if df[x_axis].dtype == 'object' or pd.api.types.is_categorical_dtype(df[x_axis]) else 'Q'
        y_type = 'Q' if pd.api.types.is_numeric_dtype(df[y_axis]) else 'N'

        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X(f'{x_axis}:{x_type}', title=x_axis),
            y=alt.Y(f'{y_axis}:{y_type}', title=y_axis)
        ).properties(
            title=f'Gráfico de {y_axis} por {x_axis}',
            height=400
        )

        if color_axis and color_axis != "None":
            color_type = 'N' if df[color_axis].dtype == 'object' or pd.api.types.is_categorical_dtype(df[color_axis]) else 'Q'
            chart = chart.encode(color=alt.Color(f'{color_axis}:{color_type}', title=color_axis))
        
        return chart
    except Exception as e:
        # En un entorno real, registrarías este error
        # st.error(f"Error al generar el gráfico: {e}")
        return None
