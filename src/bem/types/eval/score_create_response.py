# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .eval_score_run_status import EvalScoreRunStatus

__all__ = ["ScoreCreateResponse"]


class ScoreCreateResponse(BaseModel):
    """Returned by `POST /v3/eval/score`."""

    score_run_id: str = FieldInfo(alias="scoreRunID")
    """Run identifier. Use with `GET /v3/eval/score/{scoreRunID}`."""

    status: EvalScoreRunStatus
    """Status values for an eval-score run."""
