# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

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

    op: Literal["ls", "find", "open", "cat", "grep", "xref", "stat", "head"]
    """Operations exposed by `POST /v3/fs`.

    The verbs and their flag names mirror Unix tools so an LLM agent's existing
    vocabulary maps directly:

    - `ls` — list parsed documents
    - `cat` — read one parsed doc (optionally sliced by range / projected by select)
    - `grep` — substring or regex search across parse outputs
    - `head` — first N sections of one doc
    - `stat` — metadata only (page count, section count, parsed at, ...)
    - `find` — list canonical entities (cross-doc memory)
    - `open` — entity + mentions
    - `xref` — entity → sections across docs that mention it

    Doc-level ops (ls, cat, grep, head, stat) work on every parsed document,
    regardless of how the parse function was configured.

    Memory-level ops (find, open, xref) operate on the global entities table which
    is only populated when the parse function had `linkAcrossDocuments: true`. On
    environments with no memory-linked docs they return empty data with a hint
    pointing at the toggle.
    """

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
