import pandas as pd

def delete_none(df):
    
    return df.dropna(axis=1, how='all').dropna(axis=0, how='all')