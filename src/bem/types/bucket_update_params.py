# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BucketUpdateParams"]


class BucketUpdateParams(TypedDict, total=False):
    description: str
    """New description."""

    name: str
    """New name."""
