"""
This is a boilerplate pipeline 'data_validation'
generated using Kedro 1.3.0
"""

from kedro.pipeline import Node, Pipeline  # noqa
from .nodes import validate_dataset

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
                func=validate_dataset,
                inputs=[
                    "dataset_integrado",
                    "consultas_limpio"
                ],
                outputs="validation_report",
                name="validate_integrated_dataset_node",
            )
    ])
