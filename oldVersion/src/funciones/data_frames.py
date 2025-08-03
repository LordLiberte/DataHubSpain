import pandas as pd

# Este método carga datos y los devuelve como un DataFrame de pandas.
# Soporta archivos en formato .xlsx y .csv.
def cargar_datos(archivo):
    
    if archivo.endswith('.xlsx'):
        df = pd.read_excel(archivo)
        
    elif archivo.endswith('.csv'):
        df = pd.read_csv(archivo, delimiter=';')
        
    else:
        raise ValueError("Formato de archivo no soportado. Use .xlsx o .csv")
    
    # Limpieza de datos
    df = limpiezaData(df)
    return df


# Elimina las celdas en blanco de un DataFrame de pandas.
def limpiezaData(dataframe):
    
    # Reemplaza los espacios en blanco con NaN y luego elimina las filas con NaN
    for column in dataframe.columns:
        for i in range(len(dataframe[column])):
            if dataframe[column][i] == " ":
                dataframe[column][i] = pd.NA
                
        for row in dataframe[column]:
            row = str(row).strip()
                
    dataframe = dataframe.dropna()
    
    return dataframe
    