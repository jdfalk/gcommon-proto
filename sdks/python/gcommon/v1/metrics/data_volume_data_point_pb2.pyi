import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataVolumeDataPoint(_message.Message):
    __slots__ = ("timestamp", "total_bytes", "total_metrics", "total_data_points", "ingestion_rate")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_METRICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    INGESTION_RATE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    total_bytes: int
    total_metrics: int
    total_data_points: int
    ingestion_rate: float
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_bytes: _Optional[int] = ..., total_metrics: _Optional[int] = ..., total_data_points: _Optional[int] = ..., ingestion_rate: _Optional[float] = ...) -> None: ...
