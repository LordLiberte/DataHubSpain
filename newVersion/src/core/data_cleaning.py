import pandas as pd
import numpy as np
import streamlit as st # Added for debugging

# Elimina los valores NaN
def delete_none(df):
    st.write(f"DEBUG: DataFrame shape BEFORE cleaning: {df.shape}")
    # Replace Python's None with numpy's NaN for compatibility with dropna
    df = df.replace({None: np.nan})
    # Drop columns and then rows that are completely empty
    cleaned_df = df.dropna(axis=1, how='all').dropna(axis=0, how='all')
    st.write(f"DEBUG: DataFrame shape AFTER cleaning: {cleaned_df.shape}")
    return cleaned_df