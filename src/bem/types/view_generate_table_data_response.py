# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ViewGenerateTableDataResponse", "Row", "RowColumn"]


class RowColumn(BaseModel):
    """A single column entry in a view table data row"""

    column_name: str = FieldInfo(alias="columnName")
    """Name of the column"""

    value: Union[str, float, bool, List[object], object, object]
    """Value of the column (can be any JSON type)"""


class Row(BaseModel):
    """A single row in the view table data response"""

    columns: List[RowColumn]
    """Column entries for this row"""

    event_id: str = FieldInfo(alias="eventID")
    """
    Externally-stable KSUID of the event whose underlying transformation produced
    this row.
    """


class ViewGenerateTableDataResponse(BaseModel):
    """Response containing paginated view table data"""

    rows: List[Row]
    """Array of rows matching the view configuration"""

    total_count: int = FieldInfo(alias="totalCount")
    """Total number of rows matching the view (before pagination)"""
