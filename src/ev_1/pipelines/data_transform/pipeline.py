"""
This is a boilerplate pipeline 'data_transform'
generated using Kedro 1.3.0
"""

from kedro.pipeline import Node, Pipeline  # noqa
from .nodes import transform_datasets

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
                func=transform_datasets,
                inputs=[
                    "consultas_limpio",
                    "examenes_limpio",
                    "medicamentos_limpio",
                    "pacientes_limpio",
                ],
                outputs="dataset_integrado",
                name="transform_integrated_dataset_node",
            )
    ])
