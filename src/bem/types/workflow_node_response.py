# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .function_version_identifier import FunctionVersionIdentifier

__all__ = ["WorkflowNodeResponse"]


class WorkflowNodeResponse(BaseModel):
    """Read representation of a call-site node."""

    function: FunctionVersionIdentifier
    """Function (and version) executing at this call site."""

    name: str
    """Name of this call site, unique within the workflow version."""
