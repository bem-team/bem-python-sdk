# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .call import Call
from .._models import BaseModel

__all__ = ["CallGetResponse"]


class CallGetResponse(BaseModel):
    call: Optional[Call] = None
    """A workflow call returned by the V3 API.

    Compared to the V2 `Call` model:

    - Terminal outputs are split into `outputs` (non-error events) and `errors`
      (error events)
    - `callType` and function-scoped fields are removed — V3 calls are always
      workflow calls
    - The deprecated `functionCalls` field is removed (use
      `GET /v3/calls/{callID}/trace`)
    - `url` and `traceUrl` hint fields are included for resource discovery
    """

    error: Optional[str] = None
    """
    Error message if the call retrieval failed, or if the call itself failed when
    using `wait=true`.
    """
