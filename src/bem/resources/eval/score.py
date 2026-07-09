# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.eval import score_create_params
from ..._base_client import make_request_options
from ...types.eval.eval_score_run import EvalScoreRun
from ...types.eval.score_create_response import ScoreCreateResponse
from ...types.eval.eval_match_config_param import EvalMatchConfigParam

__all__ = ["ScoreResource", "AsyncScoreResource"]


class ScoreResource(SyncAPIResource):
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
    def with_raw_response(self) -> ScoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ScoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return ScoreResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        function_name: str,
        pairs: Iterable[score_create_params.Pair],
        function_version_num: int | Omit = omit,
        match_config: EvalMatchConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoreCreateResponse:
        """
        **Score a function against a list of (input, expected) pairs.**

        Submits a batch of `(input, expected)` pairs, runs the named function over each
        input, and returns per-pair + aggregate accuracy metrics comparing the
        function's actual output to the provided expected JSON.

        Scoring runs asynchronously. The response carries a `scoreRunID`; poll
        `GET /v3/eval/score/{scoreRunID}` until `status` is one of `completed`, `error`,
        or `cancelled`.

        `matchConfig` controls comparator behavior:

        - `numericTolerance`: relative tolerance for numeric fields (0 = exact)
        - `stringMatch`: `exact` (default) or `fuzzy` (Levenshtein ratio)
        - `arrayMatch`: `by-index` (default; only mode in P0)
        - `ignorePaths`: JSON Pointer paths to skip, supports `*` wildcards

        Args:
          function_name: Name of the function to score. Must be of type extract, transform, or analyze.

          pairs: Up to 1000 pairs per request.

          function_version_num: Optional version number to score against. P0: only the function's current
              version is accepted; passing a different version returns 422.

          match_config: Comparator configuration. All fields optional; conservative defaults.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/eval/score",
            body=maybe_transform(
                {
                    "function_name": function_name,
                    "pairs": pairs,
                    "function_version_num": function_version_num,
                    "match_config": match_config,
                },
                score_create_params.ScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreCreateResponse,
        )

    def retrieve(
        self,
        score_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvalScoreRun:
        """
        **Get the status and per-pair results of a score run.**

        Returns `aggregate` only once `status` reaches `completed`. `perPair` is
        populated incrementally — each pair's `fieldResults` appears as its underlying
        function call terminates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_id:
            raise ValueError(f"Expected a non-empty value for `score_run_id` but received {score_run_id!r}")
        return self._get(
            path_template("/v3/eval/score/{score_run_id}", score_run_id=score_run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalScoreRun,
        )

    def cancel(
        self,
        score_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvalScoreRun:
        """**Cancel an in-flight score run.**

        Transitions the run to `cancelled`.

        Function calls already in flight are allowed
        to finish (best-effort cancellation via the job queue); results from completed
        pairs may still appear in subsequent GETs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_id:
            raise ValueError(f"Expected a non-empty value for `score_run_id` but received {score_run_id!r}")
        return self._post(
            path_template("/v3/eval/score/{score_run_id}/cancel", score_run_id=score_run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalScoreRun,
        )


class AsyncScoreResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncScoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncScoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncScoreResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        function_name: str,
        pairs: Iterable[score_create_params.Pair],
        function_version_num: int | Omit = omit,
        match_config: EvalMatchConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoreCreateResponse:
        """
        **Score a function against a list of (input, expected) pairs.**

        Submits a batch of `(input, expected)` pairs, runs the named function over each
        input, and returns per-pair + aggregate accuracy metrics comparing the
        function's actual output to the provided expected JSON.

        Scoring runs asynchronously. The response carries a `scoreRunID`; poll
        `GET /v3/eval/score/{scoreRunID}` until `status` is one of `completed`, `error`,
        or `cancelled`.

        `matchConfig` controls comparator behavior:

        - `numericTolerance`: relative tolerance for numeric fields (0 = exact)
        - `stringMatch`: `exact` (default) or `fuzzy` (Levenshtein ratio)
        - `arrayMatch`: `by-index` (default; only mode in P0)
        - `ignorePaths`: JSON Pointer paths to skip, supports `*` wildcards

        Args:
          function_name: Name of the function to score. Must be of type extract, transform, or analyze.

          pairs: Up to 1000 pairs per request.

          function_version_num: Optional version number to score against. P0: only the function's current
              version is accepted; passing a different version returns 422.

          match_config: Comparator configuration. All fields optional; conservative defaults.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/eval/score",
            body=await async_maybe_transform(
                {
                    "function_name": function_name,
                    "pairs": pairs,
                    "function_version_num": function_version_num,
                    "match_config": match_config,
                },
                score_create_params.ScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreCreateResponse,
        )

    async def retrieve(
        self,
        score_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvalScoreRun:
        """
        **Get the status and per-pair results of a score run.**

        Returns `aggregate` only once `status` reaches `completed`. `perPair` is
        populated incrementally — each pair's `fieldResults` appears as its underlying
        function call terminates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_id:
            raise ValueError(f"Expected a non-empty value for `score_run_id` but received {score_run_id!r}")
        return await self._get(
            path_template("/v3/eval/score/{score_run_id}", score_run_id=score_run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalScoreRun,
        )

    async def cancel(
        self,
        score_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvalScoreRun:
        """**Cancel an in-flight score run.**

        Transitions the run to `cancelled`.

        Function calls already in flight are allowed
        to finish (best-effort cancellation via the job queue); results from completed
        pairs may still appear in subsequent GETs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_id:
            raise ValueError(f"Expected a non-empty value for `score_run_id` but received {score_run_id!r}")
        return await self._post(
            path_template("/v3/eval/score/{score_run_id}/cancel", score_run_id=score_run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalScoreRun,
        )


class ScoreResourceWithRawResponse:
    def __init__(self, score: ScoreResource) -> None:
        self._score = score

        self.create = to_raw_response_wrapper(
            score.create,
        )
        self.retrieve = to_raw_response_wrapper(
            score.retrieve,
        )
        self.cancel = to_raw_response_wrapper(
            score.cancel,
        )


class AsyncScoreResourceWithRawResponse:
    def __init__(self, score: AsyncScoreResource) -> None:
        self._score = score

        self.create = async_to_raw_response_wrapper(
            score.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            score.retrieve,
        )
        self.cancel = async_to_raw_response_wrapper(
            score.cancel,
        )


class ScoreResourceWithStreamingResponse:
    def __init__(self, score: ScoreResource) -> None:
        self._score = score

        self.create = to_streamed_response_wrapper(
            score.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            score.retrieve,
        )
        self.cancel = to_streamed_response_wrapper(
            score.cancel,
        )


class AsyncScoreResourceWithStreamingResponse:
    def __init__(self, score: AsyncScoreResource) -> None:
        self._score = score

        self.create = async_to_streamed_response_wrapper(
            score.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            score.retrieve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            score.cancel,
        )
