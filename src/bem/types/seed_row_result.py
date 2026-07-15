# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SeedRowResult"]


class SeedRowResult(BaseModel):
    """The outcome of seeding one row."""

    canonical: str
    """The canonical name from the input row."""

    outcome: Literal["created", "merged-with", "rejected"]
    """
    What happened to this row: `created` (new entity), `merged-with` (matched an
    existing entity), or `rejected` (see `reason`).
    """

    entity_id: Optional[str] = FieldInfo(alias="entityID", default=None)
    """Public ID (`ent_...`) of the created or merged entity. Absent when rejected."""

    reason: Optional[str] = None
    """Human-readable explanation when `outcome` is `rejected`."""
