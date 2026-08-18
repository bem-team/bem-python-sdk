# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from pydantic import Field as FieldInfo

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncFunctionsPage",
    "AsyncFunctionsPage",
    "SyncWorkflowsPage",
    "AsyncWorkflowsPage",
    "SyncCallsPage",
    "AsyncCallsPage",
    "SyncOutputsPage",
    "AsyncOutputsPage",
    "SyncErrorsPage",
    "AsyncErrorsPage",
    "SyncWorkflowVersionsPage",
    "AsyncWorkflowVersionsPage",
    "SyncViewsPage",
    "AsyncViewsPage",
    "SyncBucketsPage",
    "AsyncBucketsPage",
    "SyncCollectionsPage",
    "AsyncCollectionsPage",
]

_T = TypeVar("_T")


@runtime_checkable
class FunctionsPageItem(Protocol):
    function_id: Optional[str]


@runtime_checkable
class WorkflowsPageItem(Protocol):
    id: Optional[str]


@runtime_checkable
class CallsPageItem(Protocol):
    call_id: Optional[str]


@runtime_checkable
class OutputsPageItem(Protocol):
    event_id: Optional[str]


@runtime_checkable
class ErrorsPageItem(Protocol):
    event_id: Optional[str]


@runtime_checkable
class WorkflowVersionsPageItem(Protocol):
    version_num: Optional[int]


@runtime_checkable
class ViewsPageItem(Protocol):
    view_id: Optional[str]


@runtime_checkable
class BucketsPageItem(Protocol):
    bucket_id: Optional[str]


class SyncFunctionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    functions: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        functions = self.functions
        if not functions:
            return []
        return functions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        functions = self.functions
        if not functions:
            return None

        if is_forwards:
            item = cast(Any, functions[-1])
            if not isinstance(item, FunctionsPageItem) or item.function_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.function_id})
        else:
            item = cast(Any, self.functions[0])
            if not isinstance(item, FunctionsPageItem) or item.function_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.function_id})


class AsyncFunctionsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    functions: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        functions = self.functions
        if not functions:
            return []
        return functions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        functions = self.functions
        if not functions:
            return None

        if is_forwards:
            item = cast(Any, functions[-1])
            if not isinstance(item, FunctionsPageItem) or item.function_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.function_id})
        else:
            item = cast(Any, self.functions[0])
            if not isinstance(item, FunctionsPageItem) or item.function_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.function_id})


class SyncWorkflowsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    workflows: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        workflows = self.workflows
        if not workflows:
            return []
        return workflows

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        workflows = self.workflows
        if not workflows:
            return None

        if is_forwards:
            item = cast(Any, workflows[-1])
            if not isinstance(item, WorkflowsPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.id})
        else:
            item = cast(Any, self.workflows[0])
            if not isinstance(item, WorkflowsPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.id})


class AsyncWorkflowsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    workflows: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        workflows = self.workflows
        if not workflows:
            return []
        return workflows

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        workflows = self.workflows
        if not workflows:
            return None

        if is_forwards:
            item = cast(Any, workflows[-1])
            if not isinstance(item, WorkflowsPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.id})
        else:
            item = cast(Any, self.workflows[0])
            if not isinstance(item, WorkflowsPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.id})


class SyncCallsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    calls: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        calls = self.calls
        if not calls:
            return []
        return calls

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        calls = self.calls
        if not calls:
            return None

        if is_forwards:
            item = cast(Any, calls[-1])
            if not isinstance(item, CallsPageItem) or item.call_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.call_id})
        else:
            item = cast(Any, self.calls[0])
            if not isinstance(item, CallsPageItem) or item.call_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.call_id})


class AsyncCallsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    calls: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        calls = self.calls
        if not calls:
            return []
        return calls

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        calls = self.calls
        if not calls:
            return None

        if is_forwards:
            item = cast(Any, calls[-1])
            if not isinstance(item, CallsPageItem) or item.call_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.call_id})
        else:
            item = cast(Any, self.calls[0])
            if not isinstance(item, CallsPageItem) or item.call_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.call_id})


class SyncOutputsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    outputs: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        outputs = self.outputs
        if not outputs:
            return []
        return outputs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        outputs = self.outputs
        if not outputs:
            return None

        if is_forwards:
            item = cast(Any, outputs[-1])
            if not isinstance(item, OutputsPageItem) or item.event_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.event_id})
        else:
            item = cast(Any, self.outputs[0])
            if not isinstance(item, OutputsPageItem) or item.event_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.event_id})


class AsyncOutputsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    outputs: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        outputs = self.outputs
        if not outputs:
            return []
        return outputs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        outputs = self.outputs
        if not outputs:
            return None

        if is_forwards:
            item = cast(Any, outputs[-1])
            if not isinstance(item, OutputsPageItem) or item.event_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.event_id})
        else:
            item = cast(Any, self.outputs[0])
            if not isinstance(item, OutputsPageItem) or item.event_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.event_id})


class SyncErrorsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    errors: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        errors = self.errors
        if not errors:
            return []
        return errors

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        errors = self.errors
        if not errors:
            return None

        if is_forwards:
            item = cast(Any, errors[-1])
            if not isinstance(item, ErrorsPageItem) or item.event_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.event_id})
        else:
            item = cast(Any, self.errors[0])
            if not isinstance(item, ErrorsPageItem) or item.event_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.event_id})


class AsyncErrorsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    errors: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        errors = self.errors
        if not errors:
            return []
        return errors

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        errors = self.errors
        if not errors:
            return None

        if is_forwards:
            item = cast(Any, errors[-1])
            if not isinstance(item, ErrorsPageItem) or item.event_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.event_id})
        else:
            item = cast(Any, self.errors[0])
            if not isinstance(item, ErrorsPageItem) or item.event_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.event_id})


class SyncWorkflowVersionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    versions: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        versions = self.versions
        if not versions:
            return []
        return versions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        versions = self.versions
        if not versions:
            return None

        if is_forwards:
            item = cast(Any, versions[-1])
            if not isinstance(item, WorkflowVersionsPageItem) or item.version_num is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.version_num})
        else:
            item = cast(Any, self.versions[0])
            if not isinstance(item, WorkflowVersionsPageItem) or item.version_num is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.version_num})


class AsyncWorkflowVersionsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    versions: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        versions = self.versions
        if not versions:
            return []
        return versions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        versions = self.versions
        if not versions:
            return None

        if is_forwards:
            item = cast(Any, versions[-1])
            if not isinstance(item, WorkflowVersionsPageItem) or item.version_num is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.version_num})
        else:
            item = cast(Any, self.versions[0])
            if not isinstance(item, WorkflowVersionsPageItem) or item.version_num is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.version_num})


class SyncViewsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    views: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        views = self.views
        if not views:
            return []
        return views

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        views = self.views
        if not views:
            return None

        if is_forwards:
            item = cast(Any, views[-1])
            if not isinstance(item, ViewsPageItem) or item.view_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.view_id})
        else:
            item = cast(Any, self.views[0])
            if not isinstance(item, ViewsPageItem) or item.view_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.view_id})


class AsyncViewsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    views: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        views = self.views
        if not views:
            return []
        return views

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        views = self.views
        if not views:
            return None

        if is_forwards:
            item = cast(Any, views[-1])
            if not isinstance(item, ViewsPageItem) or item.view_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.view_id})
        else:
            item = cast(Any, self.views[0])
            if not isinstance(item, ViewsPageItem) or item.view_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.view_id})


class SyncBucketsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    buckets: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        buckets = self.buckets
        if not buckets:
            return []
        return buckets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        buckets = self.buckets
        if not buckets:
            return None

        if is_forwards:
            item = cast(Any, buckets[-1])
            if not isinstance(item, BucketsPageItem) or item.bucket_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.bucket_id})
        else:
            item = cast(Any, self.buckets[0])
            if not isinstance(item, BucketsPageItem) or item.bucket_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.bucket_id})


class AsyncBucketsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    buckets: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        buckets = self.buckets
        if not buckets:
            return []
        return buckets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        buckets = self.buckets
        if not buckets:
            return None

        if is_forwards:
            item = cast(Any, buckets[-1])
            if not isinstance(item, BucketsPageItem) or item.bucket_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.bucket_id})
        else:
            item = cast(Any, self.buckets[0])
            if not isinstance(item, BucketsPageItem) or item.bucket_id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.bucket_id})


class SyncCollectionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    collections: List[_T]
    page: Optional[int] = None
    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        collections = self.collections
        if not collections:
            return []
        return collections

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        total_pages = self.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncCollectionsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    collections: List[_T]
    page: Optional[int] = None
    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        collections = self.collections
        if not collections:
            return []
        return collections

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        total_pages = self.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})
