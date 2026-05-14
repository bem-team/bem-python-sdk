# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionCompareMetricsParams"]


class FunctionCompareMetricsParams(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of the function to compare versions for"""

    baseline_version_num: Annotated[int, PropertyInfo(alias="baselineVersionNum")]
    """**Baseline version number for comparison**

    If not provided, defaults to the previous version (current - 1).
    """

    comparison_version_num: Annotated[int, PropertyInfo(alias="comparisonVersionNum")]
    """**Comparison version number**

    If not provided, defaults to the current version.
    """

    is_regression: Annotated[bool, PropertyInfo(alias="isRegression")]
    """**Whether to compare regression test data only**

    If true, only compares transformations marked as regression tests.
    """
