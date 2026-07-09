# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .file_input_param import FileInputParam
from .eval_match_config_param import EvalMatchConfigParam

__all__ = ["ScoreCreateParams", "Pair"]


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

    match_config: Annotated[EvalMatchConfigParam, PropertyInfo(alias="matchConfig")]
    """Comparator configuration. All fields optional; conservative defaults."""


class Pair(TypedDict, total=False):
    """One `(input, expected)` pair."""

    expected: Required[object]
    """Expected output for this input, as a JSON value.

    The comparator walks `expected ∪ actual` and produces a per-leaf classification.
    """

    input: Required[FileInputParam]
    """A single file input with base64-encoded content.

    When using the Bem CLI, use `@path/to/file` in the `inputContent` field to
    automatically read and base64-encode the file:
    `--input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' --wait`
    """
