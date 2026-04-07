"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.3.0
"""

from kedro.pipeline import Node, Pipeline  # noqa
from .nodes import clean_consultas

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
             Node(
                func=clean_consultas,
                inputs="consultas",
                outputs="consultas_limpio",
                name="clean_consultas_node",
            ),
    ])
