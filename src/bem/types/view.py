# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .view_column import ViewColumn
from .view_filter import ViewFilter
from .view_aggregation import ViewAggregation
from .function_identifier import FunctionIdentifier

__all__ = ["View"]


class View(BaseModel):
    """
    A view is a table visualization of transformations that allows customers to have insight into their transformations
    """

    aggregations: List[ViewAggregation]
    """List of aggregations defined for the view"""

    columns: List[ViewColumn]
    """List of columns in the view"""

    current_version_num: int = FieldInfo(alias="currentVersionNum")
    """Current version number of the view"""

    filters: List[ViewFilter]
    """List of filters applied to the view"""

    functions: List[FunctionIdentifier]
    """List of functions that this view queries transformations from"""

    name: str
    """Name of the view"""

    view_id: str = FieldInfo(alias="viewID")
    """Unique identifier of the view"""

    description: Optional[str] = None
    """Description of the view"""
