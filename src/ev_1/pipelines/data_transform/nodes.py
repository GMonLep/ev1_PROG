"""
This is a boilerplate pipeline 'data_transform'
generated using Kedro 1.3.0
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler


def transform_datasets(
    consultas_limpio,
    examenes_limpio,
    medicamentos_limpio,
    pacientes_limpio,
):

    #juntar tablas

    df = consultas_limpio.merge(
        pacientes_limpio,
        on="paciente_id",
        how="left"
    )

    df = df.merge(
        examenes_limpio,
        on="consulta_id",
        how="left"
    )

    df = df.merge(
        medicamentos_limpio,
        on="consulta_id",
        how="left"
    )

    #funciones derivadas

    if "fecha_consulta" in df.columns:
        df["anio_consulta"] = df["fecha_consulta"].dt.year
        df["mes_consulta"] = df["fecha_consulta"].dt.month

    
    if "edad" in df.columns:
        df["edad_grupo"] = pd.cut(
            df["edad"],
            bins=[0,18,35,60,100],
            labels=["niño","joven","adulto","mayor"]
        )

    #agrupaciones

    consultas_por_paciente = (
        df.groupby("paciente_id")
        .size()
        .reset_index(name="total_consultas")
    )

    df = df.merge(consultas_por_paciente, on="paciente_id")

    if "tipo_examen" in df.columns:
        pivot_examenes = pd.pivot_table(
            df,
            index="paciente_id",
            columns="tipo_examen",
            values="resultado",
            aggfunc="count",
            fill_value=0
        ).reset_index()

        df = df.merge(pivot_examenes, on="paciente_id", how="left")
        
    #columnas numericas normalizadas

    numeric_cols = df.select_dtypes(include="number").columns

    scaler = StandardScaler()

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    #variables categoricas

    categorical_cols = df.select_dtypes(include="object").columns

    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df