# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .reviewer import Reviewer
from ..._models import BaseModel

__all__ = ["ReviewerListResponse"]


class ReviewerListResponse(BaseModel):
    """Response body for listing the reviewers of an entity type."""

    reviewers: List[Reviewer]
