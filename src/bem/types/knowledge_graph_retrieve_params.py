# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["KnowledgeGraphRetrieveParams"]


class KnowledgeGraphRetrieveParams(TypedDict, total=False):
    bucket: str
    """
    Optional bucket public ID (`bkt_...`) to scope the read to one bucket. Omit for
    the unscoped (all account+environment) view.
    """

    cursor: str
    """Cursor: return edges whose KSUID sorts after this value."""

    limit: int
    """Maximum number of edges per page (default 50, max 200)."""

    search: str
    """Case-insensitive substring match on canonical names.

    Both endpoints of an edge must match for the edge (and its nodes) to be
    returned.
    """

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only edges created at/after this RFC 3339 timestamp."""

    type: SequenceNotStr[str]
    """Restrict to entities of these types.

    An edge is returned only when BOTH of its endpoints survive the type filter.
    """
