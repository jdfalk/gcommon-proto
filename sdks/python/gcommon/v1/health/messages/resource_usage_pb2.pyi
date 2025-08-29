from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceUsage(_message.Message):
    __slots__ = ("collected_at", "component_name", "cpu", "memory", "disk", "network")
    COLLECTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    collected_at: _timestamp_pb2.Timestamp
    component_name: str
    cpu: CpuUsage
    memory: MemoryUsage
    disk: DiskUsage
    network: NetworkUsage
    def __init__(self, collected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., component_name: _Optional[str] = ..., cpu: _Optional[_Union[CpuUsage, _Mapping]] = ..., memory: _Optional[_Union[MemoryUsage, _Mapping]] = ..., disk: _Optional[_Union[DiskUsage, _Mapping]] = ..., network: _Optional[_Union[NetworkUsage, _Mapping]] = ...) -> None: ...

class CpuUsage(_message.Message):
    __slots__ = ("usage_percent", "cores", "load_average")
    USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CORES_FIELD_NUMBER: _ClassVar[int]
    LOAD_AVERAGE_FIELD_NUMBER: _ClassVar[int]
    usage_percent: float
    cores: int
    load_average: float
    def __init__(self, usage_percent: _Optional[float] = ..., cores: _Optional[int] = ..., load_average: _Optional[float] = ...) -> None: ...

class MemoryUsage(_message.Message):
    __slots__ = ("used_bytes", "total_bytes", "usage_percent")
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    used_bytes: int
    total_bytes: int
    usage_percent: float
    def __init__(self, used_bytes: _Optional[int] = ..., total_bytes: _Optional[int] = ..., usage_percent: _Optional[float] = ...) -> None: ...

class DiskUsage(_message.Message):
    __slots__ = ("used_bytes", "total_bytes", "usage_percent")
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    used_bytes: int
    total_bytes: int
    usage_percent: float
    def __init__(self, used_bytes: _Optional[int] = ..., total_bytes: _Optional[int] = ..., usage_percent: _Optional[float] = ...) -> None: ...

class NetworkUsage(_message.Message):
    __slots__ = ("bytes_received", "bytes_sent", "active_connections")
    BYTES_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    bytes_received: int
    bytes_sent: int
    active_connections: int
    def __init__(self, bytes_received: _Optional[int] = ..., bytes_sent: _Optional[int] = ..., active_connections: _Optional[int] = ...) -> None: ...
