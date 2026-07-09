# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .view_column_param import ViewColumnParam
from .view_filter_param import ViewFilterParam
from .view_aggregation_param import ViewAggregationParam
from .function_identifier_param import FunctionIdentifierParam

__all__ = ["ViewCreateParams"]


class ViewCreateParams(TypedDict, total=False):
    aggregations: Required[Iterable[ViewAggregationParam]]
    """List of aggregations defined for the view"""

    columns: Required[Iterable[ViewColumnParam]]
    """List of columns in the view"""

    filters: Required[Iterable[ViewFilterParam]]
    """List of filters applied to the view"""

    functions: Required[Iterable[FunctionIdentifierParam]]
    """List of functions that this view queries transformations from"""

    name: Required[str]
    """Name of the view"""

    description: str
    """Description of the view"""
