# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.eval import result_retrieve_results_params
from ..._base_client import make_request_options
from ...types.eval.evaluation_results import EvaluationResults

__all__ = ["ResultsResource", "AsyncResultsResource"]


class ResultsResource(SyncAPIResource):
    """
    Monitor, evaluate, and iterate on the quality of every function in your
    environment. Function Accuracy bundles two complementary loops:

    ## Evaluations (`/v3/eval`)

    Trigger and retrieve per-transformation evaluations. Evaluations run
    asynchronously and score each transformation's output against the
    function's schema for confidence, per-field hallucination detection,
    and relevance. Supported for `extract`, `transform`, `analyze`, and
    `join` events.

    1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs.
    2. **Poll** — `GET /v3/eval/results` returns the current state of each
       requested ID, partitioned into `results`, `pending`, and `failed`.
       Accepts either `eventIDs` (preferred) or `transformationIDs` as a
       comma-separated query parameter, and always keys the response by
       event KSUID.

    Up to 100 IDs may be submitted per request.

    ## Metrics, review, regression (`/v3/functions/{metrics,review,regression,compare}`)

    Roll evaluation results and user corrections up into actionable
    function-level signal:

    - **`GET /v3/functions/metrics`** — aggregate accuracy, precision,
      recall, F1, and confusion-matrix counts per function.
    - **`POST /v3/functions/review`** — sample-size estimation,
      confidence-bucketed distribution, PR-AUC, and per-threshold
      confidence intervals (Wald or Wilson) for picking review cutoffs.
    - **`POST /v3/functions/regression`** — replay corrected historical
      inputs against a new function version, producing a labeled
      regression dataset.
    - **`POST /v3/functions/regression/corrections`** — propagate
      baseline corrections onto the regression dataset so it can be
      scored.
    - **`POST /v3/functions/compare`** — compute aggregate and
      field-level lift between any two versions, optionally scoped to
      the regression dataset.

    All five endpoints support `extract` end-to-end on both the vision
    and OCR paths, alongside the legacy `transform` / `analyze` / `join`
    types.
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

    def retrieve_results(
        self,
        *,
        evaluation_version: str | Omit = omit,
        event_ids: str | Omit = omit,
        transformation_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationResults:
        """
        **Fetch evaluation results for a batch of events.**

        Pass either `eventIDs` (preferred — the externally-stable V3 identifier) or
        `transformationIDs` as a comma-separated query parameter. Exactly one of the two
        must be provided. Up to 100 IDs per request.

        For each requested ID the response reports one of three states: a completed
        `result`, still-`pending`, or `failed`. Results, pending, and failed entries are
        all keyed by event KSUID regardless of which input form was used.

        Args:
          evaluation_version: Optional evaluation version filter.

          event_ids: Comma-separated list of event KSUIDs to fetch results for. Between 1 and 100 IDs
              per request. Mutually exclusive with `transformationIDs`.

          transformation_ids: Comma-separated list of transformation IDs to fetch results for. Between 1 and
              100 IDs per request. Mutually exclusive with `eventIDs`. Prefer `eventIDs` for
              new integrations.

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
                        "evaluation_version": evaluation_version,
                        "event_ids": event_ids,
                        "transformation_ids": transformation_ids,
                    },
                    result_retrieve_results_params.ResultRetrieveResultsParams,
                ),
            ),
            cast_to=EvaluationResults,
        )


class AsyncResultsResource(AsyncAPIResource):
    """
    Monitor, evaluate, and iterate on the quality of every function in your
    environment. Function Accuracy bundles two complementary loops:

    ## Evaluations (`/v3/eval`)

    Trigger and retrieve per-transformation evaluations. Evaluations run
    asynchronously and score each transformation's output against the
    function's schema for confidence, per-field hallucination detection,
    and relevance. Supported for `extract`, `transform`, `analyze`, and
    `join` events.

    1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs.
    2. **Poll** — `GET /v3/eval/results` returns the current state of each
       requested ID, partitioned into `results`, `pending`, and `failed`.
       Accepts either `eventIDs` (preferred) or `transformationIDs` as a
       comma-separated query parameter, and always keys the response by
       event KSUID.

    Up to 100 IDs may be submitted per request.

    ## Metrics, review, regression (`/v3/functions/{metrics,review,regression,compare}`)

    Roll evaluation results and user corrections up into actionable
    function-level signal:

    - **`GET /v3/functions/metrics`** — aggregate accuracy, precision,
      recall, F1, and confusion-matrix counts per function.
    - **`POST /v3/functions/review`** — sample-size estimation,
      confidence-bucketed distribution, PR-AUC, and per-threshold
      confidence intervals (Wald or Wilson) for picking review cutoffs.
    - **`POST /v3/functions/regression`** — replay corrected historical
      inputs against a new function version, producing a labeled
      regression dataset.
    - **`POST /v3/functions/regression/corrections`** — propagate
      baseline corrections onto the regression dataset so it can be
      scored.
    - **`POST /v3/functions/compare`** — compute aggregate and
      field-level lift between any two versions, optionally scoped to
      the regression dataset.

    All five endpoints support `extract` end-to-end on both the vision
    and OCR paths, alongside the legacy `transform` / `analyze` / `join`
    types.
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

    async def retrieve_results(
        self,
        *,
        evaluation_version: str | Omit = omit,
        event_ids: str | Omit = omit,
        transformation_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationResults:
        """
        **Fetch evaluation results for a batch of events.**

        Pass either `eventIDs` (preferred — the externally-stable V3 identifier) or
        `transformationIDs` as a comma-separated query parameter. Exactly one of the two
        must be provided. Up to 100 IDs per request.

        For each requested ID the response reports one of three states: a completed
        `result`, still-`pending`, or `failed`. Results, pending, and failed entries are
        all keyed by event KSUID regardless of which input form was used.

        Args:
          evaluation_version: Optional evaluation version filter.

          event_ids: Comma-separated list of event KSUIDs to fetch results for. Between 1 and 100 IDs
              per request. Mutually exclusive with `transformationIDs`.

          transformation_ids: Comma-separated list of transformation IDs to fetch results for. Between 1 and
              100 IDs per request. Mutually exclusive with `eventIDs`. Prefer `eventIDs` for
              new integrations.

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
                        "evaluation_version": evaluation_version,
                        "event_ids": event_ids,
                        "transformation_ids": transformation_ids,
                    },
                    result_retrieve_results_params.ResultRetrieveResultsParams,
                ),
            ),
            cast_to=EvaluationResults,
        )


class ResultsResourceWithRawResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve_results = to_raw_response_wrapper(
            results.retrieve_results,
        )


class AsyncResultsResourceWithRawResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve_results = async_to_raw_response_wrapper(
            results.retrieve_results,
        )


class ResultsResourceWithStreamingResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve_results = to_streamed_response_wrapper(
            results.retrieve_results,
        )


class AsyncResultsResourceWithStreamingResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve_results = async_to_streamed_response_wrapper(
            results.retrieve_results,
        )
