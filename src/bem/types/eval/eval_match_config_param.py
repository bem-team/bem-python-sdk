# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EvalMatchConfigParam"]


class EvalMatchConfigParam(TypedDict, total=False):
    """Comparator configuration. All fields optional; conservative defaults."""

    array_match: Annotated[Literal["by-index"], PropertyInfo(alias="arrayMatch")]
    """P0 supports only `by-index`."""

    fuzzy_threshold: Annotated[float, PropertyInfo(alias="fuzzyThreshold")]
    """Levenshtein-ratio threshold used when `stringMatch == "fuzzy"`. Range `[0, 1]`.

    Default `0.85`.
    """

    ignore_paths: Annotated[SequenceNotStr[str], PropertyInfo(alias="ignorePaths")]
    """JSON Pointer paths to skip during comparison.

    The asterisk character matches arbitrary object keys / array indices.

    Example values: /metadata, /lineItems with asterisk segment, etc.
    """

    numeric_tolerance: Annotated[float, PropertyInfo(alias="numericTolerance")]
    """Relative tolerance for numeric fields.

    `0` (default) means exact equality; `0.01` means ±1%.
    """

    string_match: Annotated[Literal["exact", "fuzzy"], PropertyInfo(alias="stringMatch")]
    """`exact` (default) or `fuzzy`."""
