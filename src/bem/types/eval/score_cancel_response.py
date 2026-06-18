# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScoreCancelResponse", "MatchConfig", "PerPair", "PerPairFieldResult", "Progress", "Aggregate"]


class MatchConfig(BaseModel):
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


class PerPairFieldResult(BaseModel):
    """One leaf in `expected ∪ actual`."""

    match: Literal["exact", "within_tolerance", "fuzzy_match", "miss", "extra"]
    """Classification:

    - `exact`: both present and deep-equal
    - `within_tolerance`: both numbers, within configured tolerance
    - `fuzzy_match`: both strings, Levenshtein ratio above threshold
    - `miss`: expected present, actual absent or different
    - `extra`: actual present, expected absent
    """

    path: str
    """JSON Pointer to the leaf."""

    actual: Optional[object] = None

    delta: Optional[float] = None
    """Populated for numeric comparisons; `actual - expected`."""

    expected: Optional[object] = None


class PerPair(BaseModel):
    """Per-pair result."""

    pair_index: int = FieldInfo(alias="pairIndex")

    status: Literal["pending", "running", "completed", "failed"]
    """Per-pair status."""

    call_id: Optional[str] = FieldInfo(alias="callID", default=None)
    """The function call that produced the actual output, if any."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Error message if the underlying function call failed."""

    field_results: Optional[List[PerPairFieldResult]] = FieldInfo(alias="fieldResults", default=None)
    """Per-leaf comparator output. Present only after the pair has been compared."""


class Progress(BaseModel):
    """Counts across all pairs."""

    completed: int

    failed: int

    total: int


class Aggregate(BaseModel):
    """Aggregate accuracy metrics."""

    exact_matches: int = FieldInfo(alias="exactMatches")

    extras: int

    f1: float

    fuzzy_matches: int = FieldInfo(alias="fuzzyMatches")

    misses: int

    precision: float

    recall: float

    total_fields_actual: int = FieldInfo(alias="totalFieldsActual")

    total_fields_expected: int = FieldInfo(alias="totalFieldsExpected")

    within_tolerance: int = FieldInfo(alias="withinTolerance")


class ScoreCancelResponse(BaseModel):
    """Full status payload returned by `GET /v3/eval/score/{scoreRunID}`."""

    function_name: str = FieldInfo(alias="functionName")

    function_version_num: int = FieldInfo(alias="functionVersionNum")

    match_config: MatchConfig = FieldInfo(alias="matchConfig")
    """Comparator configuration. All fields optional; conservative defaults."""

    per_pair: List[PerPair] = FieldInfo(alias="perPair")
    """Per-pair results. `fieldResults` appears once a pair has been compared."""

    progress: Progress
    """Counts across all pairs."""

    score_run_id: str = FieldInfo(alias="scoreRunID")

    status: Literal["pending", "initializing", "running", "completed", "error", "cancelled"]
    """Status values for an eval-score run."""

    aggregate: Optional[Aggregate] = None
    """Aggregate accuracy metrics."""
