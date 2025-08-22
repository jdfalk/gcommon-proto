from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceDataPoint(_message.Message):
    __slots__ = ("timestamp", "memory_usage_percent", "cpu_usage_percent", "disk_usage_percent", "network_bytes_per_second")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DISK_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    memory_usage_percent: float
    cpu_usage_percent: float
    disk_usage_percent: float
    network_bytes_per_second: int
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., memory_usage_percent: _Optional[float] = ..., cpu_usage_percent: _Optional[float] = ..., disk_usage_percent: _Optional[float] = ..., network_bytes_per_second: _Optional[int] = ...) -> None: ...
