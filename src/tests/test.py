import pandas as pd

archivo = "data/Demografia/PoblacionResFechaSexoEdad.xlsx"
dataframe = pd.read_excel(archivo)

print(dataframe.isna().sum())