# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ClassificationListItem", "Origin", "OriginEmail", "Regex"]


class OriginEmail(BaseModel):
    patterns: Optional[List[str]] = None


class Origin(BaseModel):
    email: Optional[OriginEmail] = None


class Regex(BaseModel):
    patterns: Optional[List[str]] = None


class ClassificationListItem(BaseModel):
    name: str

    description: Optional[str] = None

    function_id: Optional[str] = FieldInfo(alias="functionID", default=None)

    function_name: Optional[str] = FieldInfo(alias="functionName", default=None)

    is_error_fallback: Optional[bool] = FieldInfo(alias="isErrorFallback", default=None)

    origin: Optional[Origin] = None

    regex: Optional[Regex] = None
