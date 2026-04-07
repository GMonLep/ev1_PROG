"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines.data_ingestion import create_pipeline as data_ingestion
from .pipelines.data_cleaning import create_pipeline as data_cleaning 
from .pipelines.data_transform import create_pipeline as data_transform 
from .pipelines.data_validation import create_pipeline as data_validation 

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines(raise_errors=True)
    pipelines["data_ingestion"] =  data_ingestion()
    pipelines["data_cleaning"] =  data_cleaning()
    pipelines["data_transform"] =  data_transform()
    pipelines["data_validation"] =  data_validation()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
