# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScoreCreateResponse"]


class ScoreCreateResponse(BaseModel):
    """Returned by `POST /v3/eval/score`."""

    score_run_id: str = FieldInfo(alias="scoreRunID")
    """Run identifier. Use with `GET /v3/eval/score/{scoreRunID}`."""

    status: Literal["pending", "initializing", "running", "completed", "error", "cancelled"]
    """Status values for an eval-score run."""
