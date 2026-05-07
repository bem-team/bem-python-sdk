# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import FsOp, f_navigate_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.fs_op import FsOp
from .._base_client import make_request_options
from ..types.f_navigate_response import FNavigateResponse

__all__ = ["FsResource", "AsyncFsResource"]


class FsResource(SyncAPIResource):
    """Unix-shell-style nav over parsed documents and the cross-doc memory store.

    `POST /v3/fs` is a single op-driven endpoint designed for LLM agents
    and programmatic consumers that want to walk a corpus the way they'd
    walk a filesystem.

    ## Doc-level ops (every parsed document)

    - `ls` — list parsed documents with rich per-doc metadata.
    - `cat` — read one doc's parse JSON, sliced (`range`) or projected (`select`).
    - `head` — first N sections of one doc.
    - `grep` — substring or regex search; `scope`, `path`, `countOnly` available.
    - `stat` — metadata only (page/section/entity counts, timestamps).

    ## Memory-level ops (require `linkAcrossDocuments: true` on the parse function)

    - `find` — list canonical entities across the corpus.
    - `open` — entity + mentions.
    - `xref` — for one entity, sections across docs that mention it (with content).

    Memory ops return an empty list with a `hint` when no docs in this
    environment have been memory-linked.

    ## Pagination

    List ops paginate by cursor — pass the previous response's `nextCursor`
    back as `cursor`; `hasMore: false` signals the last page. Same idiom as
    `/v3/calls` and `/v3/outputs`.
    """

    @cached_property
    def with_raw_response(self) -> FsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return FsResourceWithStreamingResponse(self)

    def navigate(
        self,
        *,
        op: FsOp,
        count_only: bool | Omit = omit,
        cursor: str | Omit = omit,
        filter: f_navigate_params.Filter | Omit = omit,
        ignore_case: bool | Omit = omit,
        limit: int | Omit = omit,
        n: int | Omit = omit,
        path: str | Omit = omit,
        pattern: str | Omit = omit,
        range: f_navigate_params.Range | Omit = omit,
        regex: bool | Omit = omit,
        scope: str | Omit = omit,
        select: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FNavigateResponse:
        """
        **Navigate parsed documents and the cross-doc memory store via Unix-shell
        verbs.**

        `POST /v3/fs` is a single op-driven endpoint that lets an LLM agent (or any
        programmatic client) walk a corpus the way it would walk a filesystem — `ls` to
        list, `cat` to read, `grep` to search, `head` for a quick peek, `stat` for
        metadata, and `find` / `open` / `xref` for the cross-doc entity memory layer.

        The body always carries an `op` field; other fields apply per op. The response
        envelope is uniform: `{op, data, hasMore?, nextCursor?, count?, hint?}`.

        ## Quick reference

        | Op     | `path`                    | Other fields                    | What it does                              |
        | ------ | ------------------------- | ------------------------------- | ----------------------------------------- |
        | `ls`   | —                         | `filter`, `limit`, `cursor`     | List parsed documents                     |
        | `grep` | referenceID _(optional)_  | `pattern`, `scope`, `countOnly` | Search across documents                   |
        | `cat`  | referenceID               | `range`, `select`               | Read a document's parsed content          |
        | `head` | referenceID               | `n`                             | First N sections (default 10)             |
        | `stat` | referenceID _or_ entityID | —                               | Metadata only                             |
        | `find` | —                         | `filter`, `limit`, `cursor`     | List canonical entities                   |
        | `open` | entityID                  | —                               | Entity detail + all mentions              |
        | `xref` | entityID                  | `limit`, `cursor`               | Sections across docs mentioning an entity |

        **`path`** is the positional identifier. For doc ops (`cat`, `head`, `stat`),
        pass a `referenceID` from `ls`. For entity ops (`open`, `xref`), pass an
        `entityID` from `find`. `grep` optionally takes a `path` to scope search to one
        document.

        ## Examples

        **List documents:** `{"op": "ls"}`

        **Search one document:**
        `{"op": "grep", "path": "my-doc-001", "pattern": "holiday", "scope": "sections"}`

        **Read one page:** `{"op": "cat", "path": "my-doc-001", "range": {"page": 7}}`

        **Read a page range:**
        `{"op": "cat", "path": "my-doc-001", "range": {"pageRange": [5, 10]}}`

        **Project section labels and pages only:**
        `{"op": "cat", "path": "my-doc-001", "select": ["sections.label", "sections.page", "sections.type"]}`

        **Preview first 5 sections:** `{"op": "head", "path": "my-doc-001", "n": 5}`

        **Document metadata:** `{"op": "stat", "path": "my-doc-001"}`

        **List entities:** `{"op": "find"}`

        **Entity detail + mentions:** `{"op": "open", "path": "ent_abc123"}`

        **Cross-document sections for an entity:**
        `{"op": "xref", "path": "ent_abc123"}`

        ## Key details

        `range` is an **object** with optional keys: `page` (integer), `pageRange`
        (two-element array `[from, to]`), `sectionTypes` (array of strings like
        `["table", "heading"]`).

        `select` is an **array of strings** — dotted paths like
        `["sections.label", "sections.page"]`.

        `scope` (grep) is one of `"sections"`, `"entities"`, `"relationships"`, or
        `"all"` (default).

        ## Pagination

        List ops (`ls`, `find`) paginate by cursor: pass the last item's `nextCursor`
        from a previous response to fetch the next page; `hasMore: false` signals the
        last page. Same idiom as `/v3/calls` and `/v3/outputs`.

        Args:
          op: Operations exposed by `POST /v3/fs`.

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

          count_only: When true, return only the hit count without snippet payload. Cheaper than
              fetching matches when the agent only wants a yes/no.

          cursor: Pagination cursor. Pass the last item's ID from a previous response
              (`nextCursor`) to fetch the next page.

          filter: Filter options for `op=ls` and `op=find`.

          ignore_case: When true (default), substring/regex matching is case-insensitive.

          limit: Maximum results to return. Defaults vary per op (25–50).

          n: First-N count for `op=head`. Defaults to 10.

          path:
              Identifier for ops that operate on a single resource:

              - cat / head / stat: a parsed document, by `referenceID` or `transformationID`.
              - open / xref / stat: an entity, by `entityID`.

          pattern: Substring or regex pattern for `op=grep`.

          range: Slice the parse output along page or section dimensions. Used with `op=cat`.

          regex: When true, `pattern` is interpreted as a Go regex. Default false.

          scope: Restricts grep to one part of the parse output. One of `"sections"`,
              `"entities"`, `"relationships"`, `"all"` (default).

          select: Project the parse output to specific dotted paths (e.g.
              `["sections.label", "sections.page"]`), letting an agent map a doc's structure
              cheaply before reading content. Used with `op=cat`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/fs",
            body=maybe_transform(
                {
                    "op": op,
                    "count_only": count_only,
                    "cursor": cursor,
                    "filter": filter,
                    "ignore_case": ignore_case,
                    "limit": limit,
                    "n": n,
                    "path": path,
                    "pattern": pattern,
                    "range": range,
                    "regex": regex,
                    "scope": scope,
                    "select": select,
                },
                f_navigate_params.FNavigateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FNavigateResponse,
        )


class AsyncFsResource(AsyncAPIResource):
    """Unix-shell-style nav over parsed documents and the cross-doc memory store.

    `POST /v3/fs` is a single op-driven endpoint designed for LLM agents
    and programmatic consumers that want to walk a corpus the way they'd
    walk a filesystem.

    ## Doc-level ops (every parsed document)

    - `ls` — list parsed documents with rich per-doc metadata.
    - `cat` — read one doc's parse JSON, sliced (`range`) or projected (`select`).
    - `head` — first N sections of one doc.
    - `grep` — substring or regex search; `scope`, `path`, `countOnly` available.
    - `stat` — metadata only (page/section/entity counts, timestamps).

    ## Memory-level ops (require `linkAcrossDocuments: true` on the parse function)

    - `find` — list canonical entities across the corpus.
    - `open` — entity + mentions.
    - `xref` — for one entity, sections across docs that mention it (with content).

    Memory ops return an empty list with a `hint` when no docs in this
    environment have been memory-linked.

    ## Pagination

    List ops paginate by cursor — pass the previous response's `nextCursor`
    back as `cursor`; `hasMore: false` signals the last page. Same idiom as
    `/v3/calls` and `/v3/outputs`.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncFsResourceWithStreamingResponse(self)

    async def navigate(
        self,
        *,
        op: FsOp,
        count_only: bool | Omit = omit,
        cursor: str | Omit = omit,
        filter: f_navigate_params.Filter | Omit = omit,
        ignore_case: bool | Omit = omit,
        limit: int | Omit = omit,
        n: int | Omit = omit,
        path: str | Omit = omit,
        pattern: str | Omit = omit,
        range: f_navigate_params.Range | Omit = omit,
        regex: bool | Omit = omit,
        scope: str | Omit = omit,
        select: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FNavigateResponse:
        """
        **Navigate parsed documents and the cross-doc memory store via Unix-shell
        verbs.**

        `POST /v3/fs` is a single op-driven endpoint that lets an LLM agent (or any
        programmatic client) walk a corpus the way it would walk a filesystem — `ls` to
        list, `cat` to read, `grep` to search, `head` for a quick peek, `stat` for
        metadata, and `find` / `open` / `xref` for the cross-doc entity memory layer.

        The body always carries an `op` field; other fields apply per op. The response
        envelope is uniform: `{op, data, hasMore?, nextCursor?, count?, hint?}`.

        ## Quick reference

        | Op     | `path`                    | Other fields                    | What it does                              |
        | ------ | ------------------------- | ------------------------------- | ----------------------------------------- |
        | `ls`   | —                         | `filter`, `limit`, `cursor`     | List parsed documents                     |
        | `grep` | referenceID _(optional)_  | `pattern`, `scope`, `countOnly` | Search across documents                   |
        | `cat`  | referenceID               | `range`, `select`               | Read a document's parsed content          |
        | `head` | referenceID               | `n`                             | First N sections (default 10)             |
        | `stat` | referenceID _or_ entityID | —                               | Metadata only                             |
        | `find` | —                         | `filter`, `limit`, `cursor`     | List canonical entities                   |
        | `open` | entityID                  | —                               | Entity detail + all mentions              |
        | `xref` | entityID                  | `limit`, `cursor`               | Sections across docs mentioning an entity |

        **`path`** is the positional identifier. For doc ops (`cat`, `head`, `stat`),
        pass a `referenceID` from `ls`. For entity ops (`open`, `xref`), pass an
        `entityID` from `find`. `grep` optionally takes a `path` to scope search to one
        document.

        ## Examples

        **List documents:** `{"op": "ls"}`

        **Search one document:**
        `{"op": "grep", "path": "my-doc-001", "pattern": "holiday", "scope": "sections"}`

        **Read one page:** `{"op": "cat", "path": "my-doc-001", "range": {"page": 7}}`

        **Read a page range:**
        `{"op": "cat", "path": "my-doc-001", "range": {"pageRange": [5, 10]}}`

        **Project section labels and pages only:**
        `{"op": "cat", "path": "my-doc-001", "select": ["sections.label", "sections.page", "sections.type"]}`

        **Preview first 5 sections:** `{"op": "head", "path": "my-doc-001", "n": 5}`

        **Document metadata:** `{"op": "stat", "path": "my-doc-001"}`

        **List entities:** `{"op": "find"}`

        **Entity detail + mentions:** `{"op": "open", "path": "ent_abc123"}`

        **Cross-document sections for an entity:**
        `{"op": "xref", "path": "ent_abc123"}`

        ## Key details

        `range` is an **object** with optional keys: `page` (integer), `pageRange`
        (two-element array `[from, to]`), `sectionTypes` (array of strings like
        `["table", "heading"]`).

        `select` is an **array of strings** — dotted paths like
        `["sections.label", "sections.page"]`.

        `scope` (grep) is one of `"sections"`, `"entities"`, `"relationships"`, or
        `"all"` (default).

        ## Pagination

        List ops (`ls`, `find`) paginate by cursor: pass the last item's `nextCursor`
        from a previous response to fetch the next page; `hasMore: false` signals the
        last page. Same idiom as `/v3/calls` and `/v3/outputs`.

        Args:
          op: Operations exposed by `POST /v3/fs`.

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

          count_only: When true, return only the hit count without snippet payload. Cheaper than
              fetching matches when the agent only wants a yes/no.

          cursor: Pagination cursor. Pass the last item's ID from a previous response
              (`nextCursor`) to fetch the next page.

          filter: Filter options for `op=ls` and `op=find`.

          ignore_case: When true (default), substring/regex matching is case-insensitive.

          limit: Maximum results to return. Defaults vary per op (25–50).

          n: First-N count for `op=head`. Defaults to 10.

          path:
              Identifier for ops that operate on a single resource:

              - cat / head / stat: a parsed document, by `referenceID` or `transformationID`.
              - open / xref / stat: an entity, by `entityID`.

          pattern: Substring or regex pattern for `op=grep`.

          range: Slice the parse output along page or section dimensions. Used with `op=cat`.

          regex: When true, `pattern` is interpreted as a Go regex. Default false.

          scope: Restricts grep to one part of the parse output. One of `"sections"`,
              `"entities"`, `"relationships"`, `"all"` (default).

          select: Project the parse output to specific dotted paths (e.g.
              `["sections.label", "sections.page"]`), letting an agent map a doc's structure
              cheaply before reading content. Used with `op=cat`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/fs",
            body=await async_maybe_transform(
                {
                    "op": op,
                    "count_only": count_only,
                    "cursor": cursor,
                    "filter": filter,
                    "ignore_case": ignore_case,
                    "limit": limit,
                    "n": n,
                    "path": path,
                    "pattern": pattern,
                    "range": range,
                    "regex": regex,
                    "scope": scope,
                    "select": select,
                },
                f_navigate_params.FNavigateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FNavigateResponse,
        )


class FsResourceWithRawResponse:
    def __init__(self, fs: FsResource) -> None:
        self._fs = fs

        self.navigate = to_raw_response_wrapper(
            fs.navigate,
        )


class AsyncFsResourceWithRawResponse:
    def __init__(self, fs: AsyncFsResource) -> None:
        self._fs = fs

        self.navigate = async_to_raw_response_wrapper(
            fs.navigate,
        )


class FsResourceWithStreamingResponse:
    def __init__(self, fs: FsResource) -> None:
        self._fs = fs

        self.navigate = to_streamed_response_wrapper(
            fs.navigate,
        )


class AsyncFsResourceWithStreamingResponse:
    def __init__(self, fs: AsyncFsResource) -> None:
        self._fs = fs

        self.navigate = async_to_streamed_response_wrapper(
            fs.navigate,
        )
