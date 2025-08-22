from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceLimitsSummary(_message.Message):
    __slots__ = ("memory_limit_bytes", "cpu_limit_percent", "disk_limit_bytes", "network_limit_bytes_per_sec", "memory_used_bytes", "cpu_used_percent", "disk_used_bytes", "network_used_bytes_per_sec", "limits_enforced", "violations_count")
    MEMORY_LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMIT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DISK_LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_LIMIT_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    CPU_USED_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DISK_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_USED_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    LIMITS_ENFORCED_FIELD_NUMBER: _ClassVar[int]
    VIOLATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    memory_limit_bytes: int
    cpu_limit_percent: float
    disk_limit_bytes: int
    network_limit_bytes_per_sec: int
    memory_used_bytes: int
    cpu_used_percent: float
    disk_used_bytes: int
    network_used_bytes_per_sec: int
    limits_enforced: bool
    violations_count: int
    def __init__(self, memory_limit_bytes: _Optional[int] = ..., cpu_limit_percent: _Optional[float] = ..., disk_limit_bytes: _Optional[int] = ..., network_limit_bytes_per_sec: _Optional[int] = ..., memory_used_bytes: _Optional[int] = ..., cpu_used_percent: _Optional[float] = ..., disk_used_bytes: _Optional[int] = ..., network_used_bytes_per_sec: _Optional[int] = ..., limits_enforced: bool = ..., violations_count: _Optional[int] = ...) -> None: ...
