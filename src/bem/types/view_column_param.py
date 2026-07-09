# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ViewColumnParam"]


class ViewColumnParam(TypedDict, total=False):
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
