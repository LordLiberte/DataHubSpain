import matplotlib.pyplot as plt
import seaborn as sns

# Función para cargar datos desde un archivo Excel
def Grafico_Barras(dataframe, x_col, y_col):
    """
    Crea un gráfico de barras a partir de un DataFrame de pandas.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        x_col (str): El nombre de la columna para el eje x.
        y_col (str): El nombre de la columna para el eje y.

    Returns:
        matplotlib.figure.Figure: La figura del gráfico generado.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(data=dataframe, x=x_col, y=y_col)
    return plt

# Función para crear gráficos de dispersión
def Grafico_Dispersion(dataframe, x_col, y_col):
    """
    Crea un gráfico de dispersión a partir de un DataFrame de pandas.
    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        x_col (str): El nombre de la columna para el eje x.
        y_col (str): El nombre de la columna para el eje y.
    Returns:

        matplotlib.figure.Figure: La figura del gráfico generado.
    """
    plt.figure(figsize=(10, 6))
    plt.tight_layout()
    sns.scatterplot(data=dataframe, x=x_col, y=y_col)
    return plt
