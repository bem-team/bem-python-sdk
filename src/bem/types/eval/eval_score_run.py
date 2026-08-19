# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .eval_score_run_status import EvalScoreRunStatus

__all__ = ["EvalScoreRun", "PerPair", "PerPairFieldResult", "Progress", "Aggregate"]


class PerPairFieldResult(BaseModel):
    """One leaf in `expected ∪ actual`."""

    match: Literal["match", "mismatch", "missing", "extra"]
    """
    Classification, in the same vocabulary the model-comparison endpoint reports.
    Comparison is exact — a value matches or it does not:

    - `match`: both present and deep-equal
    - `mismatch`: both present, different
    - `missing`: expected present, actual absent
    - `extra`: actual present, expected absent
    """

    path: str
    """JSON Pointer to the leaf."""

    actual: Optional[object] = None

    delta: Optional[float] = None
    """Populated for every non-identical numeric pair; `actual - expected`.

    Reported as evidence only — numbers have no threshold, so a delta tells you how
    far off a value was without ever excusing it.
    """

    expected: Optional[object] = None

    similarity: Optional[float] = None
    """
    Populated for every non-identical string pair; the Levenshtein ratio in
    `[0, 1]`. Reported as evidence: it says how close a wrong value was, which never
    makes it right.
    """


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
    """Populated once `status` is `completed` or `error`."""

    extras: int

    f1: float

    matches: int

    mismatches: int

    missing: int

    precision: float

    recall: float

    total_fields_actual: int = FieldInfo(alias="totalFieldsActual")

    total_fields_expected: int = FieldInfo(alias="totalFieldsExpected")


class EvalScoreRun(BaseModel):
    """Full status payload returned by `GET /v3/eval/score/{scoreRunID}`.

    Scoring takes no configuration: a value matches the expected one or it is a miss.
    The comparison is still recomputed on every read from the stored JSON, so the
    numbers reflect the data as it is now rather than as it was when the run executed.
    """

    function_name: str = FieldInfo(alias="functionName")

    function_version_num: int = FieldInfo(alias="functionVersionNum")

    per_pair: List[PerPair] = FieldInfo(alias="perPair")
    """Per-pair results. `fieldResults` appears once a pair has an output to compare."""

    progress: Progress
    """Counts across all pairs."""

    score_run_id: str = FieldInfo(alias="scoreRunID")

    status: EvalScoreRunStatus
    """Status values for an eval-score run."""

    aggregate: Optional[Aggregate] = None
    """Populated once `status` is `completed` or `error`."""
