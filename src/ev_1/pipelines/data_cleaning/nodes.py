"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.3.0
"""
import pandas as pd
import numpy as np


def clean_consultas(consultas: pd.DataFrame) -> pd.DataFrame:
    df = consultas.copy()


    df = df.drop_duplicates()

    #valores no conocidos 
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("unknown")
        else:
            df[col] = df[col].fillna(df[col].median())

    #tipo de dato mezclado
    if "edad" in df.columns:
        df["edad"] = pd.to_numeric(df["edad"], errors="coerce")

    #formato de fecha
    if "fecha_consulta" in df.columns:
        df["fecha_consulta"] = pd.to_datetime(
            df["fecha_consulta"], errors="coerce"
        )

    #strings normalizadoss
    for col in df.select_dtypes(include="object").columns:
        df[col] = (
            df[col]
            .str.strip()
            .str.lower()
        )
        
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df = df[(df[col] >= lower) & (df[col] <= upper)]

    return df