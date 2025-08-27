from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationResourceLimits(_message.Message):
    __slots__ = ("max_cpu_percent", "max_memory_mb", "max_disk_iops", "max_network_mbps", "max_processes", "max_file_descriptors")
    MAX_CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_IOPS_FIELD_NUMBER: _ClassVar[int]
    MAX_NETWORK_MBPS_FIELD_NUMBER: _ClassVar[int]
    MAX_PROCESSES_FIELD_NUMBER: _ClassVar[int]
    MAX_FILE_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    max_cpu_percent: int
    max_memory_mb: int
    max_disk_iops: int
    max_network_mbps: int
    max_processes: int
    max_file_descriptors: int
    def __init__(self, max_cpu_percent: _Optional[int] = ..., max_memory_mb: _Optional[int] = ..., max_disk_iops: _Optional[int] = ..., max_network_mbps: _Optional[int] = ..., max_processes: _Optional[int] = ..., max_file_descriptors: _Optional[int] = ...) -> None: ...
