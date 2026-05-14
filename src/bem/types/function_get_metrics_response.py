# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FunctionGetMetricsResponse", "Function", "FunctionMetrics"]


class FunctionMetrics(BaseModel):
    accuracy: Optional[float] = None

    f1_score: Optional[float] = FieldInfo(alias="f1Score", default=None)

    fn: int

    fp: int

    precision: Optional[float] = None

    recall: Optional[float] = None

    tn: int

    tp: int


class Function(BaseModel):
    function_name: str = FieldInfo(alias="functionName")
    """The function name"""

    metrics: FunctionMetrics

    total_labeled_results: int = FieldInfo(alias="totalLabeledResults")
    """
    Number of transformations that have been labeled/evaluated for metrics
    calculation
    """

    total_results: int = FieldInfo(alias="totalResults")
    """Total number of results processed by the function"""


class FunctionGetMetricsResponse(BaseModel):
    functions: List[Function]

    total_count: int = FieldInfo(alias="totalCount")
    """Total number of functions"""
