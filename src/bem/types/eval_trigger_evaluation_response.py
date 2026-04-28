# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EvalTriggerEvaluationResponse"]


class EvalTriggerEvaluationResponse(BaseModel):
    """Summary of the trigger call.

    Evaluations run asynchronously; use
    `POST /v3/eval/results` or `GET /v3/eval/results` to poll for results.
    """

    queued: int
    """Number of evaluation jobs newly queued."""

    skipped: int
    """
    Number of transformations skipped because an evaluation job was already pending
    or already completed for them.
    """

    errors: Optional[object] = None
    """
    Map of transformation ID to human-readable error message for any transformations
    that could not be queued (e.g. not found, unsupported event type).
    """
