# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Metrics"]


class Metrics(BaseModel):
    """Comprehensive performance metrics"""

    accuracy: Optional[float] = None
    """Overall accuracy"""

    f1_score: Optional[float] = FieldInfo(alias="f1Score", default=None)
    """F1 Score (harmonic mean of precision and recall)"""

    fn: Optional[int] = None
    """False Negatives"""

    fp: Optional[int] = None
    """False Positives"""

    precision: Optional[float] = None
    """Precision (TP / (TP + FP))"""

    recall: Optional[float] = None
    """Recall (TP / (TP + FN))"""

    tn: Optional[int] = None
    """True Negatives"""

    tp: Optional[int] = None
    """True Positives"""
