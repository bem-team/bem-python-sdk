# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RegressionApplyCorrectionsResponse"]


class RegressionApplyCorrectionsResponse(BaseModel):
    """V3 response from applying baseline corrections to regression
    transformations.

    Identifiers are surfaced as event KSUIDs — the
    externally-stable IDs used everywhere else in V3 — in place of the
    internal transformation IDs returned by the V2 endpoint.
    """

    applied: int
    """Number of corrections that were applied successfully."""

    applied_event_ids: List[str] = FieldInfo(alias="appliedEventIDs")
    """
    Event KSUIDs whose underlying regression transformation had a baseline
    correction copied onto it.
    """

    errors: object
    """
    Map of event KSUID to error message for any regression rows where the correction
    could not be applied (e.g. baseline transformation not found for the row's
    reference ID).
    """

    skipped: int
    """
    Number of regression transformations that were skipped — typically because they
    already had a correction or did not have a usable reference ID.
    """
