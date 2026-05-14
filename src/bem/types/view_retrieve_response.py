# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ViewRetrieveResponse", "Aggregation", "Column", "Filter", "Function"]


class Aggregation(BaseModel):
    """An aggregation definition for a view"""

    function: Literal["count", "count_distinct", "sum", "average", "min", "max"]
    """Aggregation function to apply to a view column"""

    name: str
    """Name of the aggregation"""

    aggregate_column_name: Optional[str] = FieldInfo(alias="aggregateColumnName", default=None)
    """
    Name of the column to aggregate (required for count_distinct, sum, average, min,
    max functions)
    """

    group_by_column_name: Optional[str] = FieldInfo(alias="groupByColumnName", default=None)
    """Name of the column to group by (optional, for grouped aggregations)"""


class Column(BaseModel):
    """A column definition in a view"""

    display_order_index: int = FieldInfo(alias="displayOrderIndex")
    """Order in which this column should be displayed (0-based index)"""

    name: str
    """Name of the column"""

    value_schema_path: List[str] = FieldInfo(alias="valueSchemaPath")
    """
    JSON path to the value in the transformation output schema (e.g.,
    ["invoiceDetails", "invoiceNumber"])
    """


class Filter(BaseModel):
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


class Function(BaseModel):
    id: Optional[str] = None
    """Unique identifier of function. Provide either id or name, not both."""

    name: Optional[str] = None
    """Name of function.

    Must be UNIQUE on a per-environment basis. Provide either id or name, not both.
    """


class ViewRetrieveResponse(BaseModel):
    """
    A view is a table visualization of transformations that allows customers to have insight into their transformations
    """

    aggregations: List[Aggregation]
    """List of aggregations defined for the view"""

    columns: List[Column]
    """List of columns in the view"""

    current_version_num: int = FieldInfo(alias="currentVersionNum")
    """Current version number of the view"""

    filters: List[Filter]
    """List of filters applied to the view"""

    functions: List[Function]
    """List of functions that this view queries transformations from"""

    name: str
    """Name of the view"""

    view_id: str = FieldInfo(alias="viewID")
    """Unique identifier of the view"""

    description: Optional[str] = None
    """Description of the view"""

    display_type: Optional[Literal["table", "bar_chart", "pie_chart"]] = FieldInfo(alias="displayType", default=None)
    """Display type of the view"""
