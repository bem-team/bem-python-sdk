# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TimeWindowParam"]


class TimeWindowParam(TypedDict, total=False):
    """Time window for filtering transformations in a view"""

    end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End of the time window in ISO 8601 (RFC 3339) format in UTC"""

    start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start of the time window in ISO 8601 (RFC 3339) format in UTC"""
