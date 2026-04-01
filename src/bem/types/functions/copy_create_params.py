# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CopyCreateParams"]


class CopyCreateParams(TypedDict, total=False):
    source_function_name: Required[Annotated[str, PropertyInfo(alias="sourceFunctionName")]]
    """Name of the function to copy from. Must be a valid existing function name."""

    target_function_name: Required[Annotated[str, PropertyInfo(alias="targetFunctionName")]]
    """Name for the new copied function. Must be unique within the target environment."""

    tags: SequenceNotStr[str]
    """Optional array of tags for the copied function.

    If not provided, defaults to the source function's tags.
    """

    target_display_name: Annotated[str, PropertyInfo(alias="targetDisplayName")]
    """Optional display name for the copied function.

    If not provided, defaults to the source function's display name with " (Copy)"
    appended.
    """

    target_environment: Annotated[str, PropertyInfo(alias="targetEnvironment")]
    """Optional environment name to copy the function to.

    If not provided, the function will be copied within the same environment.
    """
