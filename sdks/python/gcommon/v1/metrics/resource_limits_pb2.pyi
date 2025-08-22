from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsResourceLimits(_message.Message):
    __slots__ = ("max_memory_bytes", "max_cpu_percent", "max_disk_bytes", "max_metrics", "max_data_points_per_metric")
    MAX_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_METRICS_FIELD_NUMBER: _ClassVar[int]
    MAX_DATA_POINTS_PER_METRIC_FIELD_NUMBER: _ClassVar[int]
    max_memory_bytes: int
    max_cpu_percent: float
    max_disk_bytes: int
    max_metrics: int
    max_data_points_per_metric: int
    def __init__(self, max_memory_bytes: _Optional[int] = ..., max_cpu_percent: _Optional[float] = ..., max_disk_bytes: _Optional[int] = ..., max_metrics: _Optional[int] = ..., max_data_points_per_metric: _Optional[int] = ...) -> None: ...
