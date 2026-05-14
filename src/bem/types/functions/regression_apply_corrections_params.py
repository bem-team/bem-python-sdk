# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RegressionApplyCorrectionsParams"]


class RegressionApplyCorrectionsParams(TypedDict, total=False):
    baseline_version_num: Required[Annotated[int, PropertyInfo(alias="baselineVersionNum")]]
    """**Baseline version number (source of corrected data)**

    The function version number that contains transformations with corrected JSON
    that should be copied to regression transformations.
    """

    comparison_version_num: Required[Annotated[int, PropertyInfo(alias="comparisonVersionNum")]]
    """**Comparison version number (target for applying corrections)**

    The function version number of regression transformations that should receive
    the corrected JSON from the baseline version.
    """

    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """**Name of the function to apply corrections for**

    Must be an existing function with both baseline and regression transformation
    data.
    """
