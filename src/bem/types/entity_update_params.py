# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EntityUpdateParams"]


class EntityUpdateParams(TypedDict, total=False):
    add_synonyms: Annotated[SequenceNotStr[str], PropertyInfo(alias="addSynonyms")]
    """Surface forms to attach as `customer_defined` synonyms."""

    assigned_type_id: Annotated[str, PropertyInfo(alias="assignedTypeID")]
    """The `ety_...` public ID of the type to assign (overriding the bem-inferred
    type).

    The empty string clears the assignment. Omit to leave unchanged.
    """

    canonical: str
    """Replace the entity's canonical surface form (re-derives its normalized form)."""

    locale: str
    """Optional BCP 47 locale tag stamped on any added synonyms."""

    remove_synonym_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="removeSynonymIDs")]
    """`esn_...` synonym IDs to soft-delete.

    Only `customer_defined` / `sme_approved` synonyms may be removed; an `extracted`
    synonym is rejected with `409`.
    """

    status: Literal["approved", "rejected"]
    """Transition the entity's curation status.

    Only `approved` or `rejected` are accepted, and only from `extracted` or
    `proposed` (any other transition is rejected with `409`).
    """
