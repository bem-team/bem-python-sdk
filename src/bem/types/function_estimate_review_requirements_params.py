# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionEstimateReviewRequirementsParams"]


class FunctionEstimateReviewRequirementsParams(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of the function to analyze"""

    confidence_levels: Annotated[Iterable[int], PropertyInfo(alias="confidenceLevels")]
    """
    Confidence levels for statistical analysis as integers representing percentages
    (e.g., [90, 95, 99] for 90%, 95%, 99%). IMPORTANT: Only integers are accepted,
    floats like 0.95 will be rejected.
    """

    confidence_method: Annotated[Literal["wald", "wilson"], PropertyInfo(alias="confidenceMethod")]
    """Confidence interval calculation method (default "wald").

    - "wald": Normal approximation method (faster, standard)
    - "wilson": Wilson score interval (more robust for extreme rates)
    """

    evaluation_version: Annotated[Literal["0.1.0-gemini"], PropertyInfo(alias="evaluationVersion")]
    """Optional evaluation version to filter evaluations by.

    Must be one of the supported versions. If not provided, defaults to
    "0.1.0-gemini".
    """

    function_version_num: Annotated[int, PropertyInfo(alias="functionVersionNum")]
    """Optional function version number to analyze.

    If not provided, uses the latest/current version of the function.
    """

    is_regression: Annotated[bool, PropertyInfo(alias="isRegression")]
    """Internal flag indicating if the request is from a regression test"""

    margin_of_error: Annotated[float, PropertyInfo(alias="marginOfError")]
    """Margin of error for statistical calculations"""

    threshold_max: Annotated[float, PropertyInfo(alias="thresholdMax")]
    """Maximum confidence threshold to analyze"""

    threshold_min: Annotated[float, PropertyInfo(alias="thresholdMin")]
    """Minimum confidence threshold to analyze"""

    threshold_step: Annotated[float, PropertyInfo(alias="thresholdStep")]
    """Step size for threshold analysis (smaller = more granular)"""
