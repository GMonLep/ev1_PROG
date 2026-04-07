"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 1.3.0
"""
import pandas as pd
import numpy as np
from io import StringIO

def explore_datasets(consultas, examenes, medicamentos, pacientes):

    datasets = {
        "consultas": consultas,
        "examenes": examenes,
        "medicamentos": medicamentos,
        "pacientes": pacientes
    }

    report_rows = []

    for name, df in datasets.items():

        buffer = StringIO()
        df.info(buf=buffer)

        report_rows.append({
            "dataset": name,
            "shape": df.shape,
            "dtypes": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "describe": df.describe(include="all").to_dict(),
            "info": buffer.getvalue(),
            "head": df.head().to_dict()
        })

    diagnostic_report = pd.DataFrame(report_rows)

    return diagnostic_report

