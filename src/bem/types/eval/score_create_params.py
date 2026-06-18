# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..input_type import InputType

__all__ = ["ScoreCreateParams", "Pair", "PairInput", "MatchConfig"]


class ScoreCreateParams(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of the function to score. Must be of type extract, transform, or analyze."""

    pairs: Required[Iterable[Pair]]
    """Up to 1000 pairs per request."""

    function_version_num: Annotated[int, PropertyInfo(alias="functionVersionNum")]
    """Optional version number to score against.

    P0: only the function's current version is accepted; passing a different version
    returns 422.
    """

    match_config: Annotated[MatchConfig, PropertyInfo(alias="matchConfig")]
    """Comparator configuration. All fields optional; conservative defaults."""


class PairInput(TypedDict, total=False):
    """A single file input with base64-encoded content.

    When using the Bem CLI, use `@path/to/file` in the `inputContent` field to
    automatically read and base64-encode the file:
    `--input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' --wait`
    """

    input_content: Required[Annotated[str, PropertyInfo(alias="inputContent")]]
    """Base64-encoded file content.

    In the Bem CLI, use `@path/to/file` to embed file contents automatically.
    """

    input_type: Required[Annotated[InputType, PropertyInfo(alias="inputType")]]
    """The input type of the content you're sending for transformation."""


class Pair(TypedDict, total=False):
    """One `(input, expected)` pair."""

    expected: Required[object]
    """Expected output for this input, as a JSON value.

    The comparator walks `expected ∪ actual` and produces a per-leaf classification.
    """

    input: Required[PairInput]
    """A single file input with base64-encoded content.

    When using the Bem CLI, use `@path/to/file` in the `inputContent` field to
    automatically read and base64-encode the file:
    `--input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' --wait`
    """


class MatchConfig(TypedDict, total=False):
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
