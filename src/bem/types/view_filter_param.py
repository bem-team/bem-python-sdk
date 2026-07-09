# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ViewFilterParam"]


class ViewFilterParam(TypedDict, total=False):
    """A filter to apply to a view column"""

    column_name: Required[Annotated[str, PropertyInfo(alias="columnName")]]
    """Name of the column to filter on"""

    filter_type: Required[
        Annotated[
            Literal[
                "equals_string",
                "equals_number",
                "less_than_number",
                "less_than_equal_number",
                "greater_than_number",
                "greater_than_equal_number",
                "is_null",
                "is_not_null",
            ],
            PropertyInfo(alias="filterType"),
        ]
    ]
    """Type of filter to apply to a view column"""

    number: Optional[float]
    """Numeric value for the filter (required for number filter types)"""

    string: Optional[str]
    """String value for the filter (required for string filter types)"""
