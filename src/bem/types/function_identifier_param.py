# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FunctionIdentifierParam"]


class FunctionIdentifierParam(TypedDict, total=False):
    id: str
    """Unique identifier of function. Provide either id or name, not both."""

    name: str
    """Name of function.

    Must be UNIQUE on a per-environment basis. Provide either id or name, not both.
    """
