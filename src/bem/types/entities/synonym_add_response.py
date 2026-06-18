# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SynonymAddResponse"]


class SynonymAddResponse(BaseModel):
    """One synonym attached to an entity."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp of the synonym (RFC 3339)."""

    normalized_text: str = FieldInfo(alias="normalizedText")
    """Lowercased, whitespace-folded form of `text`."""

    source: Literal["extracted", "customer_defined", "sme_approved"]
    """Provenance of the synonym.

    `customer_defined` and `sme_approved` synonyms are deletable; `extracted`
    synonyms are resolver-owned and cannot be deleted.
    """

    synonym_id: str = FieldInfo(alias="synonymID")
    """Stable public identifier for the synonym (`esn_...`)."""

    text: str
    """The human-readable synonym as authored."""

    locale: Optional[str] = None
    """Optional BCP 47 locale tag, when one was supplied."""
