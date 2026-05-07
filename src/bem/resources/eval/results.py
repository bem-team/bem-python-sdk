# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.eval import result_fetch_results_params, result_retrieve_results_params
from ..._base_client import make_request_options
from ...types.eval.evaluation_results import EvaluationResults

__all__ = ["ResultsResource", "AsyncResultsResource"]


class ResultsResource(SyncAPIResource):
    """Trigger and retrieve evaluations for completed transformations.

    Evaluations run asynchronously and score each transformation's output against
    the function's schema for confidence, per-field hallucination detection, and
    relevance. Evaluations are supported for `extract`, `transform`, `analyze`,
    and `join` events.

    ## Lifecycle

    1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs
       and returns immediately with `queued` / `skipped` counts plus per-ID errors.
    2. **Poll** — `POST /v3/eval/results` (body) or `GET /v3/eval/results` (query)
       returns the current state of each requested transformation, partitioned
       into `results` (completed), `pending` (still running), and `failed`
       (terminal failures or unknown transformation IDs).

    Up to 100 transformation IDs may be submitted per request.
    """

    @cached_property
    def with_raw_response(self) -> ResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return ResultsResourceWithStreamingResponse(self)

    def fetch_results(
        self,
        *,
        transformation_ids: SequenceNotStr[str],
        evaluation_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationResults:
        """
        **Fetch evaluation results for a batch of transformations (POST).**

        For each requested transformation ID the response reports one of three states: a
        completed `result`, still-`pending`, or `failed`. The POST variant accepts the
        ID list in the request body; use the `GET` variant with query parameters for
        simpler clients.

        Args:
          transformation_ids: Transformation IDs to fetch results for. Up to 100 per request.

          evaluation_version: Optional evaluation version filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/eval/results",
            body=maybe_transform(
                {
                    "transformation_ids": transformation_ids,
                    "evaluation_version": evaluation_version,
                },
                result_fetch_results_params.ResultFetchResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationResults,
        )

    def retrieve_results(
        self,
        *,
        transformation_ids: str,
        evaluation_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationResults:
        """
        **Fetch evaluation results for a batch of transformations.**

        Identical behavior to the POST variant; accepts transformation IDs as a
        comma-separated `transformationIDs` query parameter. Limited to 100 IDs per
        request.

        Args:
          transformation_ids: Comma-separated list of transformation IDs to fetch results for. Between 1 and
              100 IDs per request.

          evaluation_version: Optional evaluation version filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/eval/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "transformation_ids": transformation_ids,
                        "evaluation_version": evaluation_version,
                    },
                    result_retrieve_results_params.ResultRetrieveResultsParams,
                ),
            ),
            cast_to=EvaluationResults,
        )


class AsyncResultsResource(AsyncAPIResource):
    """Trigger and retrieve evaluations for completed transformations.

    Evaluations run asynchronously and score each transformation's output against
    the function's schema for confidence, per-field hallucination detection, and
    relevance. Evaluations are supported for `extract`, `transform`, `analyze`,
    and `join` events.

    ## Lifecycle

    1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs
       and returns immediately with `queued` / `skipped` counts plus per-ID errors.
    2. **Poll** — `POST /v3/eval/results` (body) or `GET /v3/eval/results` (query)
       returns the current state of each requested transformation, partitioned
       into `results` (completed), `pending` (still running), and `failed`
       (terminal failures or unknown transformation IDs).

    Up to 100 transformation IDs may be submitted per request.
    """

    @cached_property
    def with_raw_response(self) -> AsyncResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncResultsResourceWithStreamingResponse(self)

    async def fetch_results(
        self,
        *,
        transformation_ids: SequenceNotStr[str],
        evaluation_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationResults:
        """
        **Fetch evaluation results for a batch of transformations (POST).**

        For each requested transformation ID the response reports one of three states: a
        completed `result`, still-`pending`, or `failed`. The POST variant accepts the
        ID list in the request body; use the `GET` variant with query parameters for
        simpler clients.

        Args:
          transformation_ids: Transformation IDs to fetch results for. Up to 100 per request.

          evaluation_version: Optional evaluation version filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/eval/results",
            body=await async_maybe_transform(
                {
                    "transformation_ids": transformation_ids,
                    "evaluation_version": evaluation_version,
                },
                result_fetch_results_params.ResultFetchResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationResults,
        )

    async def retrieve_results(
        self,
        *,
        transformation_ids: str,
        evaluation_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationResults:
        """
        **Fetch evaluation results for a batch of transformations.**

        Identical behavior to the POST variant; accepts transformation IDs as a
        comma-separated `transformationIDs` query parameter. Limited to 100 IDs per
        request.

        Args:
          transformation_ids: Comma-separated list of transformation IDs to fetch results for. Between 1 and
              100 IDs per request.

          evaluation_version: Optional evaluation version filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/eval/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "transformation_ids": transformation_ids,
                        "evaluation_version": evaluation_version,
                    },
                    result_retrieve_results_params.ResultRetrieveResultsParams,
                ),
            ),
            cast_to=EvaluationResults,
        )


class ResultsResourceWithRawResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.fetch_results = to_raw_response_wrapper(
            results.fetch_results,
        )
        self.retrieve_results = to_raw_response_wrapper(
            results.retrieve_results,
        )


class AsyncResultsResourceWithRawResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.fetch_results = async_to_raw_response_wrapper(
            results.fetch_results,
        )
        self.retrieve_results = async_to_raw_response_wrapper(
            results.retrieve_results,
        )


class ResultsResourceWithStreamingResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.fetch_results = to_streamed_response_wrapper(
            results.fetch_results,
        )
        self.retrieve_results = to_streamed_response_wrapper(
            results.retrieve_results,
        )


class AsyncResultsResourceWithStreamingResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.fetch_results = async_to_streamed_response_wrapper(
            results.fetch_results,
        )
        self.retrieve_results = async_to_streamed_response_wrapper(
            results.retrieve_results,
        )
