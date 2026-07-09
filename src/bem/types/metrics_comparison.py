# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metric_comparison import MetricComparison

__all__ = ["MetricsComparison"]


class MetricsComparison(BaseModel):
    """Comparison of metrics between two versions"""

    accuracy: Optional[MetricComparison] = None
    """Comparison of a single metric between two versions"""

    f1_score: Optional[MetricComparison] = FieldInfo(alias="f1Score", default=None)
    """Comparison of a single metric between two versions"""

    precision: Optional[MetricComparison] = None
    """Comparison of a single metric between two versions"""

    recall: Optional[MetricComparison] = None
    """Comparison of a single metric between two versions"""
