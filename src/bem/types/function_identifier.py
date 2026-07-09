# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FunctionIdentifier"]


class FunctionIdentifier(BaseModel):
    id: Optional[str] = None
    """Unique identifier of function. Provide either id or name, not both."""

    name: Optional[str] = None
    """Name of function.

    Must be UNIQUE on a per-environment basis. Provide either id or name, not both.
    """
