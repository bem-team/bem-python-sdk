# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..workflow import Workflow

__all__ = ["VersionRetrieveResponse"]


class VersionRetrieveResponse(BaseModel):
    error: Optional[str] = None
    """Error message if the workflow version retrieval failed."""

    workflow: Optional[Workflow] = None
    """V3 read representation of a workflow version."""
