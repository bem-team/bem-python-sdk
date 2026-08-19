# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .file_input_param import FileInputParam

__all__ = ["ScoreCreateParams", "Pair"]


class ScoreCreateParams(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of the function to score. Must be of type extract, transform, or analyze."""

    dataset_id: Annotated[str, PropertyInfo(alias="datasetID")]
    """A saved Golden Data Set (`gds_…`) to score against.

    Mutually exclusive with `pairs`; provide exactly one. Its input / corrected /
    schema columns are resolved by column role. When it carries a `schema`-role
    column, scoring types each row against that ground-truth schema instead of the
    function's own schema — so results hold up as functions/schemas evolve.
    """

    function_version_num: Annotated[int, PropertyInfo(alias="functionVersionNum")]
    """Optional version number to score against.

    P0: only the function's current version is accepted; passing a different version
    returns 422.
    """

    pairs: Iterable[Pair]
    """
    Inline `(input, expected)` pairs to score, up to 1000 per request. Mutually
    exclusive with `datasetID`; provide exactly one.
    """


class Pair(TypedDict, total=False):
    """One `(input, expected)` pair."""

    expected: Required[object]
    """Expected output for this input, as a JSON value.

    The comparator walks `expected ∪ actual` and produces a per-leaf classification.
    """

    input: Required[FileInputParam]
    """The file input to feed into the function."""
