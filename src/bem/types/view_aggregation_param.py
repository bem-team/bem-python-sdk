# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ViewAggregationParam"]


class ViewAggregationParam(TypedDict, total=False):
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

    display_type: Annotated[Literal["table", "bar_chart", "pie_chart"], PropertyInfo(alias="displayType")]
    """How to display the aggregation results"""

    group_by_column_name: Annotated[Optional[str], PropertyInfo(alias="groupByColumnName")]
    """Name of the column to group by (optional, for grouped aggregations)"""
