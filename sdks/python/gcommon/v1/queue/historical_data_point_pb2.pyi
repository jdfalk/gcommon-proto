import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HistoricalDataPoint(_message.Message):
    __slots__ = (
        "timestamp",
        "message_count",
        "throughput",
        "average_latency_ms",
        "error_rate",
    )
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    message_count: int
    throughput: float
    average_latency_ms: float
    error_rate: float
    def __init__(
        self,
        timestamp: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        message_count: _Optional[int] = ...,
        throughput: _Optional[float] = ...,
        average_latency_ms: _Optional[float] = ...,
        error_rate: _Optional[float] = ...,
    ) -> None: ...
