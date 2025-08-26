from gcommon.v1.metrics import data_volume_data_point_pb2 as _data_volume_data_point_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataVolumeStats(_message.Message):
    __slots__ = ("total_bytes", "total_metrics", "total_data_points", "ingestion_rate_bytes_per_second", "ingestion_rate_points_per_second", "compression_ratio", "volume_timeseries")
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_METRICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    INGESTION_RATE_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    INGESTION_RATE_POINTS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_RATIO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    total_bytes: int
    total_metrics: int
    total_data_points: int
    ingestion_rate_bytes_per_second: float
    ingestion_rate_points_per_second: float
    compression_ratio: float
    volume_timeseries: _containers.RepeatedCompositeFieldContainer[_data_volume_data_point_pb2.DataVolumeDataPoint]
    def __init__(self, total_bytes: _Optional[int] = ..., total_metrics: _Optional[int] = ..., total_data_points: _Optional[int] = ..., ingestion_rate_bytes_per_second: _Optional[float] = ..., ingestion_rate_points_per_second: _Optional[float] = ..., compression_ratio: _Optional[float] = ..., volume_timeseries: _Optional[_Iterable[_Union[_data_volume_data_point_pb2.DataVolumeDataPoint, _Mapping]]] = ...) -> None: ...
