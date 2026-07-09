# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ViewFilter"]


class ViewFilter(BaseModel):
    """A filter to apply to a view column"""

    column_name: str = FieldInfo(alias="columnName")
    """Name of the column to filter on"""

    filter_type: Literal[
        "equals_string",
        "equals_number",
        "less_than_number",
        "less_than_equal_number",
        "greater_than_number",
        "greater_than_equal_number",
        "is_null",
        "is_not_null",
    ] = FieldInfo(alias="filterType")
    """Type of filter to apply to a view column"""

    number: Optional[float] = None
    """Numeric value for the filter (required for number filter types)"""

    string: Optional[str] = None
    """String value for the filter (required for string filter types)"""
