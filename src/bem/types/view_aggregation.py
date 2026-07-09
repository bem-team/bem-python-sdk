# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ViewAggregation"]


class ViewAggregation(BaseModel):
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

    display_type: Optional[Literal["table", "bar_chart", "pie_chart"]] = FieldInfo(alias="displayType", default=None)
    """How to display the aggregation results"""

    group_by_column_name: Optional[str] = FieldInfo(alias="groupByColumnName", default=None)
    """Name of the column to group by (optional, for grouped aggregations)"""
