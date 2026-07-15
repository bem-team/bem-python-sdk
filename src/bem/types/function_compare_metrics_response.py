# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metrics_details import MetricsDetails
from .metrics_comparison import MetricsComparison

__all__ = ["FunctionCompareMetricsResponse", "FieldMetricsChange"]


class FieldMetricsChange(BaseModel):
    """Comparison of field-level metrics"""

    comparison: MetricsComparison
    """Comparison of metrics between two versions"""

    field_path: str = FieldInfo(alias="fieldPath")
    """JSON pointer path to the field"""


class FunctionCompareMetricsResponse(BaseModel):
    """**Response containing metrics comparison between two function versions**

    Shows absolute differences, lift percentages, and field-level changes.
    """

    baseline_version_num: int = FieldInfo(alias="baselineVersionNum")
    """Baseline version number used for comparison"""

    comparison_version_num: int = FieldInfo(alias="comparisonVersionNum")
    """Comparison version number"""

    function_name: str = FieldInfo(alias="functionName")
    """Name of the compared function"""

    aggregate_comparison: Optional[MetricsComparison] = FieldInfo(alias="aggregateComparison", default=None)
    """Comparison of metrics between two versions"""

    baseline_metrics: Optional[MetricsDetails] = FieldInfo(alias="baselineMetrics", default=None)
    """Detailed performance metrics and analysis"""

    baseline_transformation_count: Optional[int] = FieldInfo(alias="baselineTransformationCount", default=None)
    """Number of transformations used to calculate baseline metrics"""

    comparison_metrics: Optional[MetricsDetails] = FieldInfo(alias="comparisonMetrics", default=None)
    """Detailed performance metrics and analysis"""

    comparison_transformation_count: Optional[int] = FieldInfo(alias="comparisonTransformationCount", default=None)
    """Number of transformations used to calculate comparison metrics"""

    field_metrics_changes: Optional[List[FieldMetricsChange]] = FieldInfo(alias="fieldMetricsChanges", default=None)
    """**Field-level metrics that changed significantly**

    Only includes fields where metrics changed by more than 1%.
    """

    message: Optional[str] = None
    """Optional message with additional details"""
