# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ViewUpdateParams", "Aggregation", "Column", "Filter", "Function"]


class ViewUpdateParams(TypedDict, total=False):
    aggregations: Required[Iterable[Aggregation]]
    """List of aggregations defined for the view"""

    columns: Required[Iterable[Column]]
    """List of columns in the view"""

    filters: Required[Iterable[Filter]]
    """List of filters applied to the view"""

    functions: Required[Iterable[Function]]
    """List of functions that this view queries transformations from"""

    name: Required[str]
    """Name of the view"""


class Aggregation(TypedDict, total=False):
    """An aggregation definition for a view"""

    function: Required[Literal["count", "count_distinct", "sum", "average", "min", "max"]]
    """Aggregation function to apply to a view column"""

    name: Required[str]
    """Name of the aggregation"""

    aggregate_column_name: Annotated[Optional[str], PropertyInfo(alias="aggregateColumnName")]
    """
    Name of the column to aggregate (required for count_distinct, sum, average, min,
    max functions)
    """

    group_by_column_name: Annotated[Optional[str], PropertyInfo(alias="groupByColumnName")]
    """Name of the column to group by (optional, for grouped aggregations)"""


class Column(TypedDict, total=False):
    """A column definition in a view"""

    display_order_index: Required[Annotated[int, PropertyInfo(alias="displayOrderIndex")]]
    """Order in which this column should be displayed (0-based index)"""

    name: Required[str]
    """Name of the column"""

    value_schema_path: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="valueSchemaPath")]]
    """
    JSON path to the value in the transformation output schema (e.g.,
    ["invoiceDetails", "invoiceNumber"])
    """


class Filter(TypedDict, total=False):
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


class Function(TypedDict, total=False):
    id: str
    """Unique identifier of function. Provide either id or name, not both."""

    name: str
    """Name of function.

    Must be UNIQUE on a per-environment basis. Provide either id or name, not both.
    """
