from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceUsage(_message.Message):
    __slots__ = ("memory_used_bytes", "cpu_used_percent", "disk_used_bytes", "network_bandwidth_bytes_per_sec")
    MEMORY_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    CPU_USED_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DISK_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_BANDWIDTH_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    memory_used_bytes: int
    cpu_used_percent: float
    disk_used_bytes: int
    network_bandwidth_bytes_per_sec: int
    def __init__(self, memory_used_bytes: _Optional[int] = ..., cpu_used_percent: _Optional[float] = ..., disk_used_bytes: _Optional[int] = ..., network_bandwidth_bytes_per_sec: _Optional[int] = ...) -> None: ...
