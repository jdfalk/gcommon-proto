from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ThroughputMetrics(_message.Message):
    __slots__ = ("messages_per_second_1m", "messages_per_second_5m", "messages_per_second_15m", "messages_per_second_1h", "peak_messages_per_second", "peak_timestamp")
    MESSAGES_PER_SECOND_1M_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_PER_SECOND_5M_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_PER_SECOND_15M_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_PER_SECOND_1H_FIELD_NUMBER: _ClassVar[int]
    PEAK_MESSAGES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    PEAK_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    messages_per_second_1m: float
    messages_per_second_5m: float
    messages_per_second_15m: float
    messages_per_second_1h: float
    peak_messages_per_second: float
    peak_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, messages_per_second_1m: _Optional[float] = ..., messages_per_second_5m: _Optional[float] = ..., messages_per_second_15m: _Optional[float] = ..., messages_per_second_1h: _Optional[float] = ..., peak_messages_per_second: _Optional[float] = ..., peak_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
