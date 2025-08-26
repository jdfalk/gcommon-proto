from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PerformanceMetrics(_message.Message):
    __slots__ = ("memory_used_bytes", "memory_available_bytes", "cpu_usage_percent", "disk_used_bytes", "disk_available_bytes", "network_bytes_per_second", "active_connections", "max_connections")
    MEMORY_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_AVAILABLE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DISK_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISK_AVAILABLE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    memory_used_bytes: int
    memory_available_bytes: int
    cpu_usage_percent: float
    disk_used_bytes: int
    disk_available_bytes: int
    network_bytes_per_second: float
    active_connections: int
    max_connections: int
    def __init__(self, memory_used_bytes: _Optional[int] = ..., memory_available_bytes: _Optional[int] = ..., cpu_usage_percent: _Optional[float] = ..., disk_used_bytes: _Optional[int] = ..., disk_available_bytes: _Optional[int] = ..., network_bytes_per_second: _Optional[float] = ..., active_connections: _Optional[int] = ..., max_connections: _Optional[int] = ...) -> None: ...
