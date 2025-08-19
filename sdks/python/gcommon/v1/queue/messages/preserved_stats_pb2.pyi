from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreservedStats(_message.Message):
    __slots__ = ("lifetime_message_count", "created_at", "last_config_change", "peak_message_count", "peak_throughput", "total_uptime_ms")
    LIFETIME_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_CONFIG_CHANGE_FIELD_NUMBER: _ClassVar[int]
    PEAK_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PEAK_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UPTIME_MS_FIELD_NUMBER: _ClassVar[int]
    lifetime_message_count: int
    created_at: _timestamp_pb2.Timestamp
    last_config_change: _timestamp_pb2.Timestamp
    peak_message_count: int
    peak_throughput: float
    total_uptime_ms: int
    def __init__(self, lifetime_message_count: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_config_change: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., peak_message_count: _Optional[int] = ..., peak_throughput: _Optional[float] = ..., total_uptime_ms: _Optional[int] = ...) -> None: ...
