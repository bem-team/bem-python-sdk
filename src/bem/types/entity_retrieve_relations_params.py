# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EntityRetrieveRelationsParams"]


class EntityRetrieveRelationsParams(TypedDict, total=False):
    bucket: str
    """
    Optional bucket public ID (`bkt_...`) to scope the read to one bucket. Omit for
    the unscoped (all account+environment) view.
    """

    cursor: str
    """Cursor: return edges whose KSUID sorts after this value."""

    direction: Literal["inbound", "outbound", "both"]
    """Which edges to return relative to the entity. Defaults to `both`."""

    limit: int
    """Maximum number of edges to return (default 50, max 200)."""

    relation_type: Annotated[str, PropertyInfo(alias="relationType")]
    """Exact-match filter on the relation label."""
