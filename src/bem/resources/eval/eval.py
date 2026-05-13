# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import eval_trigger_evaluation_params
from .results import (
    ResultsResource,
    AsyncResultsResource,
    ResultsResourceWithRawResponse,
    AsyncResultsResourceWithRawResponse,
    ResultsResourceWithStreamingResponse,
    AsyncResultsResourceWithStreamingResponse,
)
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
from ..._base_client import make_request_options
from ...types.eval_trigger_evaluation_response import EvalTriggerEvaluationResponse

__all__ = ["EvalResource", "AsyncEvalResource"]


class EvalResource(SyncAPIResource):
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
    def results(self) -> ResultsResource:
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
        return ResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EvalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return EvalResourceWithStreamingResponse(self)

    def trigger_evaluation(
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
    ) -> EvalTriggerEvaluationResponse:
        """
        **Queue evaluation jobs for a batch of transformations.**

        Evaluations run asynchronously and score each transformation's output against
        the function's schema for confidence, hallucination detection, and relevance.
        Transformations must belong to events of a supported type: `extract`,
        `transform`, `analyze`, or `join`.

        Returns immediately with a summary of queued vs. skipped transformations and
        per-transformation errors. Poll `GET /v3/eval/results` to retrieve results once
        evaluations complete.

        Args:
          transformation_ids: Transformation IDs to evaluate. Up to 100 per request.

          evaluation_version: Optional evaluation version (e.g. `0.1.0-gemini`). When omitted the server's
              default evaluation version is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/eval",
            body=maybe_transform(
                {
                    "transformation_ids": transformation_ids,
                    "evaluation_version": evaluation_version,
                },
                eval_trigger_evaluation_params.EvalTriggerEvaluationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalTriggerEvaluationResponse,
        )


class AsyncEvalResource(AsyncAPIResource):
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
    def results(self) -> AsyncResultsResource:
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
        return AsyncResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncEvalResourceWithStreamingResponse(self)

    async def trigger_evaluation(
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
    ) -> EvalTriggerEvaluationResponse:
        """
        **Queue evaluation jobs for a batch of transformations.**

        Evaluations run asynchronously and score each transformation's output against
        the function's schema for confidence, hallucination detection, and relevance.
        Transformations must belong to events of a supported type: `extract`,
        `transform`, `analyze`, or `join`.

        Returns immediately with a summary of queued vs. skipped transformations and
        per-transformation errors. Poll `GET /v3/eval/results` to retrieve results once
        evaluations complete.

        Args:
          transformation_ids: Transformation IDs to evaluate. Up to 100 per request.

          evaluation_version: Optional evaluation version (e.g. `0.1.0-gemini`). When omitted the server's
              default evaluation version is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/eval",
            body=await async_maybe_transform(
                {
                    "transformation_ids": transformation_ids,
                    "evaluation_version": evaluation_version,
                },
                eval_trigger_evaluation_params.EvalTriggerEvaluationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalTriggerEvaluationResponse,
        )


class EvalResourceWithRawResponse:
    def __init__(self, eval: EvalResource) -> None:
        self._eval = eval

        self.trigger_evaluation = to_raw_response_wrapper(
            eval.trigger_evaluation,
        )

    @cached_property
    def results(self) -> ResultsResourceWithRawResponse:
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
        return ResultsResourceWithRawResponse(self._eval.results)


class AsyncEvalResourceWithRawResponse:
    def __init__(self, eval: AsyncEvalResource) -> None:
        self._eval = eval

        self.trigger_evaluation = async_to_raw_response_wrapper(
            eval.trigger_evaluation,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithRawResponse:
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
        return AsyncResultsResourceWithRawResponse(self._eval.results)


class EvalResourceWithStreamingResponse:
    def __init__(self, eval: EvalResource) -> None:
        self._eval = eval

        self.trigger_evaluation = to_streamed_response_wrapper(
            eval.trigger_evaluation,
        )

    @cached_property
    def results(self) -> ResultsResourceWithStreamingResponse:
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
        return ResultsResourceWithStreamingResponse(self._eval.results)


class AsyncEvalResourceWithStreamingResponse:
    def __init__(self, eval: AsyncEvalResource) -> None:
        self._eval = eval

        self.trigger_evaluation = async_to_streamed_response_wrapper(
            eval.trigger_evaluation,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithStreamingResponse:
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
        return AsyncResultsResourceWithStreamingResponse(self._eval.results)
