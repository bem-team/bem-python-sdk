# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BucketDeleteParams"]


class BucketDeleteParams(TypedDict, total=False):
    cascade: bool
    """
    When `true`, delete the bucket even if it still contains entities (the entities
    are removed along with it). When omitted or `false`, the request is rejected
    with `409 Conflict` if the bucket is non-empty.

    The default bucket can never be deleted regardless of this flag.
    """
