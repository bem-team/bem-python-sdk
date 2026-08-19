# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .fs_op import FsOp
from .._models import BaseModel

__all__ = ["FNavigateResponse"]


class FNavigateResponse(BaseModel):
    """Uniform response shape returned for every `op`.

    `data` is op-specific
    JSON (a list, an object, or a string), but the wrapper is constant
    so a client only learns one parse path.
    """

    data: object
    """Op-specific payload. See per-op shapes below."""

    op: FsOp
    """The op echoed back."""

    count: Optional[int] = None
    """
    Set for ops that return a count rather than a list (`grep` with
    `countOnly=true`) or as a sanity check on lists.
    """

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """True when more pages exist for cursor-paginated ops."""

    hint: Optional[str] = None
    """Optional human-readable note.

    Surfaced on memory-level ops (`find` / `open` / `xref`) when the corpus has no
    memory-linked docs, pointing users at the `linkAcrossDocuments` toggle on the
    parse function.
    """

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor to pass as `cursor` in the next request to fetch the next page.

    Empty when `hasMore=false`.
    """
