import pandas as pd
import numpy as np

# Elimina los valores NaN
def delete_none(df):
    # Replace Python's None with numpy's NaN for compatibility with dropna
    df.replace({None: np.nan}, inplace=True)
    # Drop columns and then rows that are completely empty
    return df.dropna(axis=1, how='all').dropna(axis=0, how='all')