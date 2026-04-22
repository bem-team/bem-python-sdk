# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Generic, TypeVar

from ._models import GenericModel

__all__ = ["WorkflowWrapper"]

_T = TypeVar("_T")


class WorkflowWrapper(GenericModel, Generic[_T]):
    workflow: _T

    @staticmethod
    def _unwrapper(obj: "WorkflowWrapper[_T]") -> _T:
        return obj.workflow
