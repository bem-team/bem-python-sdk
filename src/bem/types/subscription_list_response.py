# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .subscription_v3 import SubscriptionV3

__all__ = ["SubscriptionListResponse"]

SubscriptionListResponse: TypeAlias = List[SubscriptionV3]
