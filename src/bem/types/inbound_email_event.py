# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InboundEmailEvent"]


class InboundEmailEvent(BaseModel):
    from_: str = FieldInfo(alias="from")
    """The email address of the sender."""

    subject: str
    """The subject of the email."""

    to: str
    """The email address of the recipient."""

    delivered_to: Optional[str] = FieldInfo(alias="deliveredTo", default=None)
    """
    The email address of the original intended recipient if the email itself was
    forwarded.
    """
