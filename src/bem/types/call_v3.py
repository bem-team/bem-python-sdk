# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .event import Event
from .._models import BaseModel
from .error_event import ErrorEvent

__all__ = ["CallV3", "Input", "InputBatchFiles", "InputBatchFilesInput", "InputSingleFile"]


class InputBatchFilesInput(BaseModel):
    input_type: Optional[str] = FieldInfo(alias="inputType", default=None)
    """Input type of the file"""

    item_reference_id: Optional[str] = FieldInfo(alias="itemReferenceID", default=None)
    """Item reference ID"""

    s3_url: Optional[str] = FieldInfo(alias="s3URL", default=None)
    """Presigned S3 URL for the file"""


class InputBatchFiles(BaseModel):
    inputs: Optional[List[InputBatchFilesInput]] = None


class InputSingleFile(BaseModel):
    input_type: Optional[str] = FieldInfo(alias="inputType", default=None)
    """Input type of the file"""

    s3_url: Optional[str] = FieldInfo(alias="s3URL", default=None)
    """Presigned S3 URL for the file"""


class Input(BaseModel):
    """Input to the main function call."""

    batch_files: Optional[InputBatchFiles] = FieldInfo(alias="batchFiles", default=None)

    single_file: Optional[InputSingleFile] = FieldInfo(alias="singleFile", default=None)


class CallV3(BaseModel):
    """A workflow call returned by the V3 API.

    Compared to the V2 `Call` model:
    - Terminal outputs are split into `outputs` (non-error events) and `errors` (error events)
    - `callType` and function-scoped fields are removed — V3 calls are always workflow calls
    - The deprecated `functionCalls` field is removed (use `GET /v3/calls/{callID}/trace`)
    - `url` and `traceUrl` hint fields are included for resource discovery
    """

    call_id: str = FieldInfo(alias="callID")
    """Unique identifier of the call."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time the call was created."""

    errors: List[ErrorEvent]
    """Terminal error events of this call.

    Workflow calls are not atomic — `errors` and `outputs` may both be non-empty if
    some enclosed function calls succeeded and others failed.

    Retrieve individual errors via `GET /v3/errors/{eventID}`.
    """

    outputs: List[Event]
    """
    Terminal non-error outputs of this call: primary events (non-split-collection)
    that did not trigger any downstream function calls. Workflow calls are not
    atomic — `outputs` and `errors` may both be non-empty if some enclosed function
    calls succeeded and others failed.

    Each element is a polymorphic event object; inspect `eventType` to determine the
    type. Retrieve individual outputs via `GET /v3/outputs/{eventID}`.
    """

    trace_url: str = FieldInfo(alias="traceUrl")
    """Hint URL for the full execution trace: `GET /v3/calls/{callID}/trace`."""

    url: str
    """Hint URL for retrieving this call: `GET /v3/calls/{callID}`."""

    call_reference_id: Optional[str] = FieldInfo(alias="callReferenceID", default=None)
    """Your reference ID for this call, propagated from the original request."""

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)
    """The date and time the call finished.

    Only set once status is `completed` or `failed`.
    """

    input: Optional[Input] = None
    """Input to the main function call."""

    status: Optional[Literal["pending", "running", "completed", "failed"]] = None
    """Status of call."""

    workflow_id: Optional[str] = FieldInfo(alias="workflowID", default=None)
    """Unique identifier of the workflow."""

    workflow_name: Optional[str] = FieldInfo(alias="workflowName", default=None)
    """Name of the workflow."""

    workflow_version_num: Optional[int] = FieldInfo(alias="workflowVersionNum", default=None)
    """Version number of the workflow."""
