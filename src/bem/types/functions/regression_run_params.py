# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RegressionRunParams"]


class RegressionRunParams(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """**Name of the function to test for regressions**

    Must be an existing function with historical transformation data containing user
    corrections. The function must be currently active and callable.
    """

    baseline_version_num: Annotated[int, PropertyInfo(alias="baselineVersionNum")]
    """**Function version number to use as baseline for comparison**

    - Defaults to `currentVersionNum - 1` (previous version)
    - Must be a valid, existing version number for the function
    - Used to retrieve historical transformation data for comparison
    - Cannot be the same as `comparisonVersionNum`
    """

    comparison_version_num: Annotated[int, PropertyInfo(alias="comparisonVersionNum")]
    """**Function version number to test against the baseline**

    - Defaults to current version number (latest version)
    - Must be a valid, existing version number for the function
    - This version will be used to create new function calls for testing
    - Cannot be the same as `baselineVersionNum`
    """

    only_corrected_data: Annotated[bool, PropertyInfo(alias="onlyCorrectedData")]
    """**Whether to only test transformations with user corrections**

    - Defaults to `true` (recommended)
    - When `true`: Only uses transformations with `correctedJSON` as ground truth
    - When `false`: May include transformations without corrections (less reliable)
    - Corrected data provides the most accurate regression testing results
    """

    sample_size: Annotated[int, PropertyInfo(alias="sampleSize")]
    """**Number of historical samples to test**

    - Defaults to 50 samples
    - Minimum: 1, Maximum: 1000
    - Only transformations with `correctedJSON` (user corrections) are eligible
    - Actual sample size may be smaller if insufficient corrected data exists
    - Larger samples provide more statistical confidence but take longer to process
    """
