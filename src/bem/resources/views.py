# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    view_list_params,
    view_create_params,
    view_update_params,
    view_generate_table_data_params,
    view_generate_aggregation_data_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.view_list_response import ViewListResponse
from ..types.view_create_response import ViewCreateResponse
from ..types.view_update_response import ViewUpdateResponse
from ..types.view_retrieve_response import ViewRetrieveResponse
from ..types.view_generate_table_data_response import ViewGenerateTableDataResponse
from ..types.view_generate_aggregation_data_response import ViewGenerateAggregationDataResponse

__all__ = ["ViewsResource", "AsyncViewsResource"]


class ViewsResource(SyncAPIResource):
    """
    Views are tabular projections over the `transformations` your functions
    produce — a saved query that turns raw extracted JSON into a
    filterable, paginatable, aggregatable table.

    ## Anatomy

    A view declares:
    - One or more **functions** to read from (by `functionID` or `functionName`).
    - A list of **columns**, each pinned to a `valueSchemaPath` (a JSON
      Pointer into the function's output schema).
    - Optional **filters** (string equality, numeric comparators,
      null-checks) and **aggregations** (`count`, `count_distinct`,
      `sum`, `average`, `min`, `max`).

    Views are versioned: every update produces a new version, and the
    previous version remains immutable and addressable. Function types
    that produce transformations with an output schema — `extract`,
    `transform`, `analyze`, `join` — are all queryable through views;
    `extract` works uniformly across vision and OCR inputs.

    ## Reading data

    - **`POST /v3/views/table-data`** — paginated rows of column values.
      Each row reports the underlying event's `eventID` (the
      externally-stable KSUID used everywhere else in V3) plus the
      projected column values.
    - **`POST /v3/views/aggregation-data`** — group-by-able aggregate
      values across the same query surface.

    Both endpoints take a `timeWindow` to bound the transformation set
    and require at least one `function` to read from.
    """

    @cached_property
    def with_raw_response(self) -> ViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return ViewsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        aggregations: Iterable[view_create_params.Aggregation],
        columns: Iterable[view_create_params.Column],
        filters: Iterable[view_create_params.Filter],
        functions: Iterable[view_create_params.Function],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewCreateResponse:
        """
        **Create a view.**

        A view is a tabular projection over the `transformations` produced by one or
        more functions. Each column declares a `valueSchemaPath` — a JSON Pointer path
        into the function's output schema — and the view can additionally carry filters
        and aggregations.

        Supported for every function type that produces correctable transformations and
        an output schema: `extract`, `transform`, `analyze`, `join`. Extract works on
        both vision (PDF/PNG/JPEG/HEIC/HEIF/WebP) and OCR-routed inputs — the resulting
        rows surface through views uniformly.

        The new view is created at `versionNum: 1`. Subsequent updates produce new
        versions; the version-1 configuration remains addressable.

        Args:
          aggregations: List of aggregations defined for the view

          columns: List of columns in the view

          filters: List of filters applied to the view

          functions: List of functions that this view queries transformations from

          name: Name of the view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/views",
            body=maybe_transform(
                {
                    "aggregations": aggregations,
                    "columns": columns,
                    "filters": filters,
                    "functions": functions,
                    "name": name,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewCreateResponse,
        )

    def retrieve(
        self,
        view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewRetrieveResponse:
        """**Retrieve a view by ID.**

        Returns the view's current version.

        To inspect a historical version, fetch the
        list of versions on the View object and re-request with the desired version
        pinned (versions are immutable once created).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._get(
            path_template("/v3/views/{view_id}", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewRetrieveResponse,
        )

    def update(
        self,
        view_id: str,
        *,
        aggregations: Iterable[view_update_params.Aggregation],
        columns: Iterable[view_update_params.Column],
        filters: Iterable[view_update_params.Filter],
        functions: Iterable[view_update_params.Function],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewUpdateResponse:
        """**Update a view.

        Updates create a new version.**

        The previous version remains addressable and immutable. The new configuration is
        fully replacing — pass the complete view body, not a patch. The version number
        is auto-incremented.

        Args:
          aggregations: List of aggregations defined for the view

          columns: List of columns in the view

          filters: List of filters applied to the view

          functions: List of functions that this view queries transformations from

          name: Name of the view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._put(
            path_template("/v3/views/{view_id}", view_id=view_id),
            body=maybe_transform(
                {
                    "aggregations": aggregations,
                    "columns": columns,
                    "filters": filters,
                    "functions": functions,
                    "name": name,
                },
                view_update_params.ViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewUpdateResponse,
        )

    def list(
        self,
        *,
        ending_before: str | Omit = omit,
        function_ids: SequenceNotStr[str] | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        view_ids: SequenceNotStr[str] | Omit = omit,
        view_name_substring: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewListResponse:
        """
        **List views in the current environment, optionally filtered by the functions
        they read from.**

        Views are tabular projections over `transformations` rows: each view names one
        or more functions and a list of columns (JSON-pointer paths into
        `extractedJson`), and produces a uniform table that can be filtered, paginated,
        and aggregated.

        Filters AND together when combined. Pagination is cursor-based on `viewID`;
        default limit is 50, maximum 100.

        Args:
          ending_before: Cursor — a `viewID` defining your place in the list.

          function_ids: Return only views that read from at least one of the named functions.

          function_names: Return only views that read from at least one of the named functions.

          sort_order: Sort order over view IDs (default `asc`).

          starting_after: Cursor — a `viewID` defining your place in the list.

          view_ids: Return only the specified view IDs.

          view_name_substring: Case-insensitive substring search over view names.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "function_ids": function_ids,
                        "function_names": function_names,
                        "limit": limit,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "view_ids": view_ids,
                        "view_name_substring": view_name_substring,
                    },
                    view_list_params.ViewListParams,
                ),
            ),
            cast_to=ViewListResponse,
        )

    def delete(
        self,
        view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Delete a view and every one of its versions.**

        Permanent.

        Any cached data-table or aggregation result clients have fetched
        remains valid, but subsequent calls to `POST /v3/views/table-data` or
        `POST /v3/views/aggregation-data` for this view will fail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/views/{view_id}", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def generate_aggregation_data(
        self,
        *,
        aggregations: Iterable[view_generate_aggregation_data_params.Aggregation],
        columns: Iterable[view_generate_aggregation_data_params.Column],
        filters: Iterable[view_generate_aggregation_data_params.Filter],
        functions: Iterable[view_generate_aggregation_data_params.Function],
        name: str,
        time_window: view_generate_aggregation_data_params.TimeWindow,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewGenerateAggregationDataResponse:
        """
        **Generate aggregation results for a view.**

        Executes each aggregation declared on the view against the `transformations`
        rows produced by the named functions inside the supplied `timeWindow`, applying
        the view's filters. Supported aggregation functions: `count`, `count_distinct`,
        `sum`, `average`, `min`, `max`. Grouped aggregations return up to 200 groups per
        aggregation; non-grouped aggregations return a single group with an empty
        `groupName`.

        As with table-data, the `functions` field is required.

        Args:
          aggregations: List of aggregations defined for the view

          columns: List of columns in the view

          filters: List of filters applied to the view

          functions: List of functions that this view queries transformations from

          name: Name of the view

          time_window: Time window for filtering transformations in a view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/views/aggregation-data",
            body=maybe_transform(
                {
                    "aggregations": aggregations,
                    "columns": columns,
                    "filters": filters,
                    "functions": functions,
                    "name": name,
                    "time_window": time_window,
                },
                view_generate_aggregation_data_params.ViewGenerateAggregationDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewGenerateAggregationDataResponse,
        )

    def generate_table_data(
        self,
        *,
        aggregations: Iterable[view_generate_table_data_params.Aggregation],
        columns: Iterable[view_generate_table_data_params.Column],
        filters: Iterable[view_generate_table_data_params.Filter],
        functions: Iterable[view_generate_table_data_params.Function],
        name: str,
        time_window: view_generate_table_data_params.TimeWindow,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewGenerateTableDataResponse:
        """
        **Generate paginated table data for a view.**

        Executes the view's query against `transformations` rows produced by the named
        functions inside the supplied `timeWindow`, applies the view's filters, and
        returns matching rows. Each row reports the event `eventID` (externally-stable
        KSUID) plus the projected column values.

        The `functions` field is required — at least one `functionID` or `functionName`
        must be supplied. `limit` defaults to 50 with a maximum of 200; `offset` is
        zero-based. The response's `totalCount` reflects the match count before
        pagination, so paging can be driven off it.

        Args:
          aggregations: List of aggregations defined for the view

          columns: List of columns in the view

          filters: List of filters applied to the view

          functions: List of functions that this view queries transformations from

          name: Name of the view

          time_window: Time window for filtering transformations in a view

          limit: Maximum number of rows to return (default: 50, max: 200)

          offset: Number of rows to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/views/table-data",
            body=maybe_transform(
                {
                    "aggregations": aggregations,
                    "columns": columns,
                    "filters": filters,
                    "functions": functions,
                    "name": name,
                    "time_window": time_window,
                    "limit": limit,
                    "offset": offset,
                },
                view_generate_table_data_params.ViewGenerateTableDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewGenerateTableDataResponse,
        )


class AsyncViewsResource(AsyncAPIResource):
    """
    Views are tabular projections over the `transformations` your functions
    produce — a saved query that turns raw extracted JSON into a
    filterable, paginatable, aggregatable table.

    ## Anatomy

    A view declares:
    - One or more **functions** to read from (by `functionID` or `functionName`).
    - A list of **columns**, each pinned to a `valueSchemaPath` (a JSON
      Pointer into the function's output schema).
    - Optional **filters** (string equality, numeric comparators,
      null-checks) and **aggregations** (`count`, `count_distinct`,
      `sum`, `average`, `min`, `max`).

    Views are versioned: every update produces a new version, and the
    previous version remains immutable and addressable. Function types
    that produce transformations with an output schema — `extract`,
    `transform`, `analyze`, `join` — are all queryable through views;
    `extract` works uniformly across vision and OCR inputs.

    ## Reading data

    - **`POST /v3/views/table-data`** — paginated rows of column values.
      Each row reports the underlying event's `eventID` (the
      externally-stable KSUID used everywhere else in V3) plus the
      projected column values.
    - **`POST /v3/views/aggregation-data`** — group-by-able aggregate
      values across the same query surface.

    Both endpoints take a `timeWindow` to bound the transformation set
    and require at least one `function` to read from.
    """

    @cached_property
    def with_raw_response(self) -> AsyncViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncViewsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        aggregations: Iterable[view_create_params.Aggregation],
        columns: Iterable[view_create_params.Column],
        filters: Iterable[view_create_params.Filter],
        functions: Iterable[view_create_params.Function],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewCreateResponse:
        """
        **Create a view.**

        A view is a tabular projection over the `transformations` produced by one or
        more functions. Each column declares a `valueSchemaPath` — a JSON Pointer path
        into the function's output schema — and the view can additionally carry filters
        and aggregations.

        Supported for every function type that produces correctable transformations and
        an output schema: `extract`, `transform`, `analyze`, `join`. Extract works on
        both vision (PDF/PNG/JPEG/HEIC/HEIF/WebP) and OCR-routed inputs — the resulting
        rows surface through views uniformly.

        The new view is created at `versionNum: 1`. Subsequent updates produce new
        versions; the version-1 configuration remains addressable.

        Args:
          aggregations: List of aggregations defined for the view

          columns: List of columns in the view

          filters: List of filters applied to the view

          functions: List of functions that this view queries transformations from

          name: Name of the view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/views",
            body=await async_maybe_transform(
                {
                    "aggregations": aggregations,
                    "columns": columns,
                    "filters": filters,
                    "functions": functions,
                    "name": name,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewCreateResponse,
        )

    async def retrieve(
        self,
        view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewRetrieveResponse:
        """**Retrieve a view by ID.**

        Returns the view's current version.

        To inspect a historical version, fetch the
        list of versions on the View object and re-request with the desired version
        pinned (versions are immutable once created).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._get(
            path_template("/v3/views/{view_id}", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewRetrieveResponse,
        )

    async def update(
        self,
        view_id: str,
        *,
        aggregations: Iterable[view_update_params.Aggregation],
        columns: Iterable[view_update_params.Column],
        filters: Iterable[view_update_params.Filter],
        functions: Iterable[view_update_params.Function],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewUpdateResponse:
        """**Update a view.

        Updates create a new version.**

        The previous version remains addressable and immutable. The new configuration is
        fully replacing — pass the complete view body, not a patch. The version number
        is auto-incremented.

        Args:
          aggregations: List of aggregations defined for the view

          columns: List of columns in the view

          filters: List of filters applied to the view

          functions: List of functions that this view queries transformations from

          name: Name of the view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._put(
            path_template("/v3/views/{view_id}", view_id=view_id),
            body=await async_maybe_transform(
                {
                    "aggregations": aggregations,
                    "columns": columns,
                    "filters": filters,
                    "functions": functions,
                    "name": name,
                },
                view_update_params.ViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewUpdateResponse,
        )

    async def list(
        self,
        *,
        ending_before: str | Omit = omit,
        function_ids: SequenceNotStr[str] | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        view_ids: SequenceNotStr[str] | Omit = omit,
        view_name_substring: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewListResponse:
        """
        **List views in the current environment, optionally filtered by the functions
        they read from.**

        Views are tabular projections over `transformations` rows: each view names one
        or more functions and a list of columns (JSON-pointer paths into
        `extractedJson`), and produces a uniform table that can be filtered, paginated,
        and aggregated.

        Filters AND together when combined. Pagination is cursor-based on `viewID`;
        default limit is 50, maximum 100.

        Args:
          ending_before: Cursor — a `viewID` defining your place in the list.

          function_ids: Return only views that read from at least one of the named functions.

          function_names: Return only views that read from at least one of the named functions.

          sort_order: Sort order over view IDs (default `asc`).

          starting_after: Cursor — a `viewID` defining your place in the list.

          view_ids: Return only the specified view IDs.

          view_name_substring: Case-insensitive substring search over view names.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ending_before": ending_before,
                        "function_ids": function_ids,
                        "function_names": function_names,
                        "limit": limit,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "view_ids": view_ids,
                        "view_name_substring": view_name_substring,
                    },
                    view_list_params.ViewListParams,
                ),
            ),
            cast_to=ViewListResponse,
        )

    async def delete(
        self,
        view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Delete a view and every one of its versions.**

        Permanent.

        Any cached data-table or aggregation result clients have fetched
        remains valid, but subsequent calls to `POST /v3/views/table-data` or
        `POST /v3/views/aggregation-data` for this view will fail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/views/{view_id}", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def generate_aggregation_data(
        self,
        *,
        aggregations: Iterable[view_generate_aggregation_data_params.Aggregation],
        columns: Iterable[view_generate_aggregation_data_params.Column],
        filters: Iterable[view_generate_aggregation_data_params.Filter],
        functions: Iterable[view_generate_aggregation_data_params.Function],
        name: str,
        time_window: view_generate_aggregation_data_params.TimeWindow,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewGenerateAggregationDataResponse:
        """
        **Generate aggregation results for a view.**

        Executes each aggregation declared on the view against the `transformations`
        rows produced by the named functions inside the supplied `timeWindow`, applying
        the view's filters. Supported aggregation functions: `count`, `count_distinct`,
        `sum`, `average`, `min`, `max`. Grouped aggregations return up to 200 groups per
        aggregation; non-grouped aggregations return a single group with an empty
        `groupName`.

        As with table-data, the `functions` field is required.

        Args:
          aggregations: List of aggregations defined for the view

          columns: List of columns in the view

          filters: List of filters applied to the view

          functions: List of functions that this view queries transformations from

          name: Name of the view

          time_window: Time window for filtering transformations in a view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/views/aggregation-data",
            body=await async_maybe_transform(
                {
                    "aggregations": aggregations,
                    "columns": columns,
                    "filters": filters,
                    "functions": functions,
                    "name": name,
                    "time_window": time_window,
                },
                view_generate_aggregation_data_params.ViewGenerateAggregationDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewGenerateAggregationDataResponse,
        )

    async def generate_table_data(
        self,
        *,
        aggregations: Iterable[view_generate_table_data_params.Aggregation],
        columns: Iterable[view_generate_table_data_params.Column],
        filters: Iterable[view_generate_table_data_params.Filter],
        functions: Iterable[view_generate_table_data_params.Function],
        name: str,
        time_window: view_generate_table_data_params.TimeWindow,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewGenerateTableDataResponse:
        """
        **Generate paginated table data for a view.**

        Executes the view's query against `transformations` rows produced by the named
        functions inside the supplied `timeWindow`, applies the view's filters, and
        returns matching rows. Each row reports the event `eventID` (externally-stable
        KSUID) plus the projected column values.

        The `functions` field is required — at least one `functionID` or `functionName`
        must be supplied. `limit` defaults to 50 with a maximum of 200; `offset` is
        zero-based. The response's `totalCount` reflects the match count before
        pagination, so paging can be driven off it.

        Args:
          aggregations: List of aggregations defined for the view

          columns: List of columns in the view

          filters: List of filters applied to the view

          functions: List of functions that this view queries transformations from

          name: Name of the view

          time_window: Time window for filtering transformations in a view

          limit: Maximum number of rows to return (default: 50, max: 200)

          offset: Number of rows to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/views/table-data",
            body=await async_maybe_transform(
                {
                    "aggregations": aggregations,
                    "columns": columns,
                    "filters": filters,
                    "functions": functions,
                    "name": name,
                    "time_window": time_window,
                    "limit": limit,
                    "offset": offset,
                },
                view_generate_table_data_params.ViewGenerateTableDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewGenerateTableDataResponse,
        )


class ViewsResourceWithRawResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_raw_response_wrapper(
            views.create,
        )
        self.retrieve = to_raw_response_wrapper(
            views.retrieve,
        )
        self.update = to_raw_response_wrapper(
            views.update,
        )
        self.list = to_raw_response_wrapper(
            views.list,
        )
        self.delete = to_raw_response_wrapper(
            views.delete,
        )
        self.generate_aggregation_data = to_raw_response_wrapper(
            views.generate_aggregation_data,
        )
        self.generate_table_data = to_raw_response_wrapper(
            views.generate_table_data,
        )


class AsyncViewsResourceWithRawResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_raw_response_wrapper(
            views.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            views.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            views.update,
        )
        self.list = async_to_raw_response_wrapper(
            views.list,
        )
        self.delete = async_to_raw_response_wrapper(
            views.delete,
        )
        self.generate_aggregation_data = async_to_raw_response_wrapper(
            views.generate_aggregation_data,
        )
        self.generate_table_data = async_to_raw_response_wrapper(
            views.generate_table_data,
        )


class ViewsResourceWithStreamingResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_streamed_response_wrapper(
            views.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            views.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            views.update,
        )
        self.list = to_streamed_response_wrapper(
            views.list,
        )
        self.delete = to_streamed_response_wrapper(
            views.delete,
        )
        self.generate_aggregation_data = to_streamed_response_wrapper(
            views.generate_aggregation_data,
        )
        self.generate_table_data = to_streamed_response_wrapper(
            views.generate_table_data,
        )


class AsyncViewsResourceWithStreamingResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_streamed_response_wrapper(
            views.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            views.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            views.update,
        )
        self.list = async_to_streamed_response_wrapper(
            views.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            views.delete,
        )
        self.generate_aggregation_data = async_to_streamed_response_wrapper(
            views.generate_aggregation_data,
        )
        self.generate_table_data = async_to_streamed_response_wrapper(
            views.generate_table_data,
        )
