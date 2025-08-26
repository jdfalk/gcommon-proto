from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSubscriptionInfoResponse(_message.Message):
    __slots__ = ("subscription_id", "subscription_name", "topic_name", "state", "consumer_group", "current_offset", "latest_offset", "unacked_count", "created_at", "last_activity", "active_consumers", "total_consumed", "consumption_rate")
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LATEST_OFFSET_FIELD_NUMBER: _ClassVar[int]
    UNACKED_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    CONSUMPTION_RATE_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    subscription_name: str
    topic_name: str
    state: str
    consumer_group: str
    current_offset: int
    latest_offset: int
    unacked_count: int
    created_at: _timestamp_pb2.Timestamp
    last_activity: _timestamp_pb2.Timestamp
    active_consumers: int
    total_consumed: int
    consumption_rate: float
    def __init__(self, subscription_id: _Optional[str] = ..., subscription_name: _Optional[str] = ..., topic_name: _Optional[str] = ..., state: _Optional[str] = ..., consumer_group: _Optional[str] = ..., current_offset: _Optional[int] = ..., latest_offset: _Optional[int] = ..., unacked_count: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_activity: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., active_consumers: _Optional[int] = ..., total_consumed: _Optional[int] = ..., consumption_rate: _Optional[float] = ...) -> None: ...
