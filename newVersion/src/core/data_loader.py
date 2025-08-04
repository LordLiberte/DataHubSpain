import pandas as pd
import os

# Carga el dataset de la subcarpeta escogida
def load_dataset(folder_path):
    
    csv_file = None
    md_file = None
    
    for f in os.listdir(folder_path):
        if f.endswith(".csv"):
            csv_file = f
        elif f.endswith(".md"):
            md_file = f

    df = None
    if csv_file:
        df = pd.read_csv(os.path.join(folder_path, csv_file))

    metadata = None
    if md_file:
        with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as f:
            metadata = f.read()
    
    return df, metadata