import pandas as pd
import numpy as np

def delete_none_any(df):
    """
    Elimina filas y columnas que contengan al menos un valor vacío.

    Esta función primero convierte celdas que contienen strings vacíos,
    espacios en blanco o valores None a NaN. Luego elimina cualquier
    columna o fila que contenga al menos un valor NaN.

    Args:
        df (pd.DataFrame): El DataFrame de pandas a limpiar.

    Returns:
        pd.DataFrame: Un nuevo DataFrame sin filas ni columnas con valores vacíos.
    """
    # Convierte strings vacíos, con solo espacios y valores None a NaN
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.replace({None: np.nan})

    # Elimina las columnas y luego las filas si tienen CUALQUIER valor NaN
    # Aquí es donde usamos `how='any'`
    cleaned_df = df.dropna(axis=1, how='any').dropna(axis=0, how='any')

    return cleaned_df

# --- Ejemplo de uso ---
if __name__ == '__main__':
    # Creando un DataFrame de ejemplo con valores vacíos parciales
    data = {'A': [1, 2, np.nan, 4, 5],
            'B': [6, 7, 8, '', 10],
            'C': ['hola', 'adios', '   ', 'python', ''],
            'D': [11, 12, 13, 14, 15],
            'E': [np.nan, np.nan, np.nan, 19, 20]}

    df = pd.DataFrame(data)

    print("DataFrame original:")
    print(df)

    # Limpiando el DataFrame con la nueva función
    df_cleaned = delete_none_any(df)

    print("\nDataFrame limpio (eliminando cualquier fila o columna con valores vacíos):")
    print(df_cleaned)
