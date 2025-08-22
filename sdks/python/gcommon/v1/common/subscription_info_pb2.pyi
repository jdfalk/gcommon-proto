from gcommon.v1.common import subscription_status_pb2 as _subscription_status_pb2
from gcommon.v1.common import client_info_pb2 as _client_info_pb2
from gcommon.v1.common import filter_options_pb2 as _filter_options_pb2
from gcommon.v1.common import subscription_options_pb2 as _subscription_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonSubscriptionInfo(_message.Message):
    __slots__ = ("subscription_id", "filter", "start_time", "end_time", "subscriber", "options", "status")
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    filter: _filter_options_pb2.FilterOptions
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    subscriber: _client_info_pb2.ClientInfo
    options: _subscription_options_pb2.SubscriptionOptions
    status: _subscription_status_pb2.SubscriptionStatus
    def __init__(self, subscription_id: _Optional[str] = ..., filter: _Optional[_Union[_filter_options_pb2.FilterOptions, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., subscriber: _Optional[_Union[_client_info_pb2.ClientInfo, _Mapping]] = ..., options: _Optional[_Union[_subscription_options_pb2.SubscriptionOptions, _Mapping]] = ..., status: _Optional[_Union[_subscription_status_pb2.SubscriptionStatus, str]] = ...) -> None: ...
