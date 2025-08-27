from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceAllocations(_message.Message):
    __slots__ = (
        "allocated_memory_bytes",
        "allocated_cpu_percent",
        "allocated_disk_bytes",
        "allocated_ports",
    )
    ALLOCATED_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_DISK_BYTES_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_PORTS_FIELD_NUMBER: _ClassVar[int]
    allocated_memory_bytes: int
    allocated_cpu_percent: float
    allocated_disk_bytes: int
    allocated_ports: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        allocated_memory_bytes: _Optional[int] = ...,
        allocated_cpu_percent: _Optional[float] = ...,
        allocated_disk_bytes: _Optional[int] = ...,
        allocated_ports: _Optional[_Iterable[int]] = ...,
    ) -> None: ...
