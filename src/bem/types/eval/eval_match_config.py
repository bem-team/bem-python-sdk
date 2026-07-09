# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EvalMatchConfig"]


class EvalMatchConfig(BaseModel):
    """Comparator configuration. All fields optional; conservative defaults."""

    array_match: Optional[Literal["by-index"]] = FieldInfo(alias="arrayMatch", default=None)
    """P0 supports only `by-index`."""

    fuzzy_threshold: Optional[float] = FieldInfo(alias="fuzzyThreshold", default=None)
    """Levenshtein-ratio threshold used when `stringMatch == "fuzzy"`. Range `[0, 1]`.

    Default `0.85`.
    """

    ignore_paths: Optional[List[str]] = FieldInfo(alias="ignorePaths", default=None)
    """JSON Pointer paths to skip during comparison.

    The asterisk character matches arbitrary object keys / array indices.

    Example values: /metadata, /lineItems with asterisk segment, etc.
    """

    numeric_tolerance: Optional[float] = FieldInfo(alias="numericTolerance", default=None)
    """Relative tolerance for numeric fields.

    `0` (default) means exact equality; `0.01` means ±1%.
    """

    string_match: Optional[Literal["exact", "fuzzy"]] = FieldInfo(alias="stringMatch", default=None)
    """`exact` (default) or `fuzzy`."""
