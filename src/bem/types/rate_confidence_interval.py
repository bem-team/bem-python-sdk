# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RateConfidenceInterval"]


class RateConfidenceInterval(BaseModel):
    """
    Confidence interval for a rate/proportion using Wald (normal approximation) method by default.

    Wald confidence intervals use the normal approximation to the binomial distribution.
    For extreme rates or small sample sizes, Wilson confidence intervals may be more appropriate.
    """

    current_sample: int = FieldInfo(alias="currentSample")
    """Current number of samples/observations available"""

    sample_needed: int = FieldInfo(alias="sampleNeeded")
    """Minimum number of samples needed for reliable confidence interval calculation"""

    ci_lower: Optional[float] = FieldInfo(alias="ciLower", default=None)
    """Lower bound of the confidence interval (null if insufficient sample size)"""

    ci_upper: Optional[float] = FieldInfo(alias="ciUpper", default=None)
    """Upper bound of the confidence interval (null if insufficient sample size)"""

    mid: Optional[float] = None
    """
    Point estimate (observed rate) at the center of the interval (null if
    insufficient sample size)
    """
