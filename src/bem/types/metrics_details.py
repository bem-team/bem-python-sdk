# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .metrics import Metrics
from .._models import BaseModel

__all__ = ["MetricsDetails", "FieldMetric"]


class FieldMetric(BaseModel):
    """Enhanced field metrics with comprehensive analytics"""

    field_path: str = FieldInfo(alias="fieldPath")
    """JSON path to the field"""

    metrics: Optional[Metrics] = None
    """Comprehensive performance metrics"""


class MetricsDetails(BaseModel):
    """Detailed performance metrics and analysis"""

    aggregate_metrics: Optional[Metrics] = FieldInfo(alias="aggregateMetrics", default=None)
    """Comprehensive performance metrics"""

    field_metrics: Optional[List[FieldMetric]] = FieldInfo(alias="fieldMetrics", default=None)
    """Enhanced field metrics with comprehensive analytics"""

    precision_recall_auc: Optional[float] = FieldInfo(alias="precisionRecallAuc", default=None)
    """Area Under the Precision-Recall Curve"""
