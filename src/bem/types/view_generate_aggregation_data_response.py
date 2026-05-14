# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ViewGenerateAggregationDataResponse", "Aggregation", "AggregationGroup"]


class AggregationGroup(BaseModel):
    """A single group result in an aggregation response"""

    group_name: str = FieldInfo(alias="groupName")
    """Name of the group (empty string for non-grouped aggregations)"""

    value: float
    """Aggregated value for this group"""


class Aggregation(BaseModel):
    """Aggregation result for a single aggregation definition"""

    groups: List[AggregationGroup]
    """Array of group results (single group for non-grouped aggregations)"""

    name: str
    """Name of the aggregation"""


class ViewGenerateAggregationDataResponse(BaseModel):
    """Response containing aggregation data for a view"""

    aggregations: List[Aggregation]
    """Array of aggregation results"""
