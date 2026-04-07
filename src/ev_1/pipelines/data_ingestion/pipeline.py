"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 1.3.0
"""

from kedro.pipeline import Node, Pipeline  # noqa
from .nodes import explore_datasets

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
                func=explore_datasets,
                inputs=[
                    "consultas",
                    "examenes",
                    "medicamentos",
                    "pacientes",
                ],
                outputs="diagnostic_report",
                name="initial_data_exploration_node",
            ),
    ])
