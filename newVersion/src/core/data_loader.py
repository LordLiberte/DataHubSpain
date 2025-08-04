import pandas as pd
import os

# Carga el dataset de la subcarpeta escogida
def load_dataset(folder_path):
    
    # Construir la ruta absoluta
    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_folder_path = os.path.abspath(os.path.join(base_dir, "..", "..", folder_path))

    data_file = None
    md_file = None
    
    # Find data file (csv or xlsx) and metadata file
    for f in os.listdir(absolute_folder_path):
        if f.endswith((".csv", ".xlsx")):
            data_file = f
        elif f.endswith(".md"):
            md_file = f

    df = None
    if data_file:
        file_path = os.path.join(absolute_folder_path, data_file)
        # Definir valores que deben ser tratados como NaN y el separador de miles
        na_vals = [' ', '']
        
        if data_file.endswith(".csv"):
            # El separador de miles puede variar, '.' es común en formatos españoles
            df = pd.read_csv(file_path, na_values=na_vals, thousands='.')
        elif data_file.endswith(".xlsx"):
            df = pd.read_excel(file_path, na_values=na_vals, thousands='.')

    metadata = None
    if md_file:
        with open(os.path.join(absolute_folder_path, md_file), "r", encoding="utf-8") as f:
            metadata = f.read()
    
    return df, metadata