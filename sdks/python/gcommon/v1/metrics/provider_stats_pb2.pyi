from gcommon.v1.metrics import resource_usage_pb2 as _resource_usage_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderStats(_message.Message):
    __slots__ = ("metrics_count", "data_points_count", "data_volume_bytes", "operations_per_second", "error_rate", "resource_usage")
    METRICS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATA_POINTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATA_VOLUME_BYTES_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    metrics_count: int
    data_points_count: int
    data_volume_bytes: int
    operations_per_second: float
    error_rate: float
    resource_usage: _resource_usage_pb2.ResourceUsage
    def __init__(self, metrics_count: _Optional[int] = ..., data_points_count: _Optional[int] = ..., data_volume_bytes: _Optional[int] = ..., operations_per_second: _Optional[float] = ..., error_rate: _Optional[float] = ..., resource_usage: _Optional[_Union[_resource_usage_pb2.ResourceUsage, _Mapping]] = ...) -> None: ...
