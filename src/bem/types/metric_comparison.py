# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetricComparison"]


class MetricComparison(BaseModel):
    """Comparison of a single metric between two versions"""

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue", default=None)
    """Value in baseline version (null if not available)"""

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)
    """Value in comparison version (null if not available)"""

    difference: Optional[float] = None
    """Absolute difference (comparisonValue - baselineValue)"""

    lift_percent: Optional[float] = FieldInfo(alias="liftPercent", default=None)
    """**Percentage change from baseline to comparison**

    Formula: ((comparisonValue - baselineValue) / baselineValue) \\** 100

    - Positive values indicate improvement
    - Negative values indicate regression
    """
