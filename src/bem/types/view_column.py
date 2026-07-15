# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ViewColumn"]


class ViewColumn(BaseModel):
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
