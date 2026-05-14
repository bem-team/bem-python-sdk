# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RegressionRunResponse", "Result", "ResultCall"]


class ResultCall(BaseModel):
    """**Call created for regression testing**

    Links the original historical reference ID to the new call ID created for testing.
    Use the call ID with standard call endpoints to monitor progress and retrieve results.
    """

    call_id: str = FieldInfo(alias="callID")
    """**New call ID created for regression testing**

    Use this ID with standard call endpoints:

    - `GET /v2/calls/{callID}` - Check status and retrieve results
    - The call will have reference ID matching the original transformation
    """

    original_reference_id: str = FieldInfo(alias="originalReferenceID")
    """**Original reference ID from historical transformation data**

    This is the reference ID that was used when the historical transformation was
    originally created. It provides traceability back to the original business
    context (e.g., invoice number, document ID).
    """


class Result(BaseModel):
    """**Detailed regression test results and tracking information**

    Contains function call IDs for monitoring progress. When all function calls complete,
    use the transformation endpoints to retrieve and analyze the actual results.
    """

    function_name: str = FieldInfo(alias="functionName")
    """**Name of the function being tested**

    The function for which regression testing was initiated.
    """

    total_samples: int = FieldInfo(alias="totalSamples")
    """**Total number of samples being tested**

    This represents the number of historical transformations found with corrections
    that will be retested with the latest function version.
    """

    calls: Optional[List[ResultCall]] = None
    """**Calls created for regression testing**

    Each object contains the original reference ID and the new call ID created for
    testing. Use these call IDs with standard call endpoints to monitor progress:

    - `GET /v2/calls/{callID}` - Check individual status
    - `GET /v2/calls?referenceIDs=regression-*` - List all regression calls
    """


class RegressionRunResponse(BaseModel):
    """**Response from initiating a regression test**

    Contains the function call IDs created for async processing and tracking information.
    Use the returned function call IDs to monitor progress and retrieve results.
    """

    function_name: str = FieldInfo(alias="functionName")
    """**Name of the function being tested**

    Echoes back the function name from the request for confirmation.
    """

    result: Result
    """**Detailed regression test results and tracking information**

    Contains function call IDs for monitoring progress. When all function calls
    complete, use the transformation endpoints to retrieve and analyze the actual
    results.
    """
