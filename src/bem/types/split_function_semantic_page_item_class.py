# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SplitFunctionSemanticPageItemClass"]


class SplitFunctionSemanticPageItemClass(BaseModel):
    name: str

    description: Optional[str] = None

    next_function_id: Optional[str] = FieldInfo(alias="nextFunctionID", default=None)
    """The unique ID of the function you want to use for this item class."""

    next_function_name: Optional[str] = FieldInfo(alias="nextFunctionName", default=None)
    """The unique name of the function you want to use for this item class."""
