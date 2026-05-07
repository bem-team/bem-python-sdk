# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .event import Event
from .._models import BaseModel

__all__ = ["OutputRetrieveResponse"]


class OutputRetrieveResponse(BaseModel):
    output: Event
    """V3 read-side event union.

    Superset of the shared `Event` union: it contains every shared variant verbatim
    (backward compatible) and adds the V3-only `extract`, `parse`, `classify`,
    `analyze`, `payload_shaping`, and `evaluation` variants. This is also the union
    delivered as the body of outbound webhook payloads.
    """
