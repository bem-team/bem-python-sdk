# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SynonymRemoveParams"]


class SynonymRemoveParams(TypedDict, total=False):
    id: Required[str]

    bucket: str
    """Optional bucket public ID (`bkt_...`) to scope the entity lookup to one bucket.

    Omit for the unscoped (all account+environment) view.
    """
