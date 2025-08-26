import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricInfo(_message.Message):
    __slots__ = ("name", "metric_type", "data_points", "data_volume_bytes", "error_rate", "last_updated")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    DATA_VOLUME_BYTES_FIELD_NUMBER: _ClassVar[int]
    ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    name: str
    metric_type: str
    data_points: int
    data_volume_bytes: int
    error_rate: float
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., metric_type: _Optional[str] = ..., data_points: _Optional[int] = ..., data_volume_bytes: _Optional[int] = ..., error_rate: _Optional[float] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
