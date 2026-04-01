# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SplitFunctionSemanticPageItemClassParam"]


class SplitFunctionSemanticPageItemClassParam(TypedDict, total=False):
    name: Required[str]

    description: str

    next_function_id: Annotated[str, PropertyInfo(alias="nextFunctionID")]
    """The unique ID of the function you want to use for this item class."""

    next_function_name: Annotated[str, PropertyInfo(alias="nextFunctionName")]
    """The unique name of the function you want to use for this item class."""
