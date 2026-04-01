# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["RouteListItemParam", "Origin", "OriginEmail", "Regex"]


class OriginEmail(TypedDict, total=False):
    patterns: SequenceNotStr[str]


class Origin(TypedDict, total=False):
    email: OriginEmail


class Regex(TypedDict, total=False):
    patterns: SequenceNotStr[str]


class RouteListItemParam(TypedDict, total=False):
    name: Required[str]

    description: str

    function_id: Annotated[str, PropertyInfo(alias="functionID")]

    function_name: Annotated[str, PropertyInfo(alias="functionName")]

    is_error_fallback: Annotated[bool, PropertyInfo(alias="isErrorFallback")]

    origin: Origin

    regex: Regex
