from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from gcommon.v1.common import subscription_info_pb2 as _subscription_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListSubscriptionsResponse(_message.Message):
    __slots__ = ("subscriptions", "next_page_token", "metadata")
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_subscription_info_pb2.CommonSubscriptionInfo]
    next_page_token: str
    metadata: _response_metadata_pb2.ResponseMetadata
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[_subscription_info_pb2.CommonSubscriptionInfo, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...
