# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .connector import Connector

__all__ = ["ConnectorListResponse"]


class ConnectorListResponse(BaseModel):
    """Response body for listing connectors."""

    connectors: List[Connector]
