"""
This is a boilerplate pipeline 'data_validation'
generated using Kedro 1.3.0
"""
import pandas as pd


def validate_dataset(dataset_integrado, consultas_limpio):

    report = {}

    #validación integridad de los datos

    report["total_rows"] = dataset_integrado.shape[0]
    report["total_columns"] = dataset_integrado.shape[1]

    report["missing_values"] = dataset_integrado.isnull().sum().sum()

    report["duplicate_rows"] = dataset_integrado.duplicated().sum()

    #validación columnas

    expected_columns = [
        "paciente_id",
        "consulta_id"
    ]

    report["missing_expected_columns"] = [
        col for col in expected_columns if col not in dataset_integrado.columns
    ]

    #antes y dsps

    report["rows_before_cleaning"] = consultas_limpio.shape[0]
    report["rows_after_transformation"] = dataset_integrado.shape[0]

    report["row_difference"] = (
        consultas_limpio.shape[0] - dataset_integrado.shape[0]
    )

    #convertir a dataframe

    validation_report = pd.DataFrame([report])

    return validation_report