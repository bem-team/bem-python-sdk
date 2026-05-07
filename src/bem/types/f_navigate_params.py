# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .fs_op import FsOp
from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["FNavigateParams", "Filter", "Range"]


class FNavigateParams(TypedDict, total=False):
    op: Required[FsOp]
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

    count_only: Annotated[bool, PropertyInfo(alias="countOnly")]
    """
    When true, return only the hit count without snippet payload. Cheaper than
    fetching matches when the agent only wants a yes/no.
    """

    cursor: str
    """Pagination cursor.

    Pass the last item's ID from a previous response (`nextCursor`) to fetch the
    next page.
    """

    filter: Filter
    """Filter options for `op=ls` and `op=find`."""

    ignore_case: Annotated[bool, PropertyInfo(alias="ignoreCase")]
    """When true (default), substring/regex matching is case-insensitive."""

    limit: int
    """Maximum results to return. Defaults vary per op (25–50)."""

    n: int
    """First-N count for `op=head`. Defaults to 10."""

    path: str
    """Identifier for ops that operate on a single resource:

    - cat / head / stat: a parsed document, by `referenceID` or `transformationID`.
    - open / xref / stat: an entity, by `entityID`.
    """

    pattern: str
    """Substring or regex pattern for `op=grep`."""

    range: Range
    """Slice the parse output along page or section dimensions. Used with `op=cat`."""

    regex: bool
    """When true, `pattern` is interpreted as a Go regex. Default false."""

    scope: str
    """Restricts grep to one part of the parse output.

    One of `"sections"`, `"entities"`, `"relationships"`, `"all"` (default).
    """

    select: SequenceNotStr[str]
    """Project the parse output to specific dotted paths (e.g.

    `["sections.label", "sections.page"]`), letting an agent map a doc's structure
    cheaply before reading content. Used with `op=cat`.
    """


class Filter(TypedDict, total=False):
    """Filter options for `op=ls` and `op=find`."""

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Match a parsed doc's source function name exactly."""

    search: str
    """Substring match on canonical name (entities) or `referenceID` (parsed docs).

    Case-insensitive.
    """

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Restrict to resources created at or after this timestamp."""

    type: str
    """Match an entity's `type` field exactly (e.g. `"drug"`, `"study"`)."""


class Range(TypedDict, total=False):
    """Slice the parse output along page or section dimensions. Used with `op=cat`."""

    page: int
    """Restrict sections to one page (1-indexed)."""

    page_range: Annotated[Iterable[int], PropertyInfo(alias="pageRange")]
    """Restrict sections to an inclusive page range.

    Two-element array of `[from, to]` (both 1-indexed).
    """

    section_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="sectionTypes")]
    """
    Keep only sections whose `type` matches one of these (e.g. `["table", "list"]`).
    """
