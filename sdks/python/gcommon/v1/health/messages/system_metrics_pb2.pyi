from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SystemMetrics(_message.Message):
    __slots__ = ("collected_at", "cpu_usage_percent", "memory_used_bytes", "memory_total_bytes", "disk_used_bytes", "disk_total_bytes", "network_bytes_received", "network_bytes_sent", "active_connections", "load_average_1m", "load_average_5m", "load_average_15m", "process_count", "uptime_seconds")
    COLLECTED_AT_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISK_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISK_TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_BYTES_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    LOAD_AVERAGE_1M_FIELD_NUMBER: _ClassVar[int]
    LOAD_AVERAGE_5M_FIELD_NUMBER: _ClassVar[int]
    LOAD_AVERAGE_15M_FIELD_NUMBER: _ClassVar[int]
    PROCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPTIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    collected_at: _timestamp_pb2.Timestamp
    cpu_usage_percent: float
    memory_used_bytes: int
    memory_total_bytes: int
    disk_used_bytes: int
    disk_total_bytes: int
    network_bytes_received: int
    network_bytes_sent: int
    active_connections: int
    load_average_1m: float
    load_average_5m: float
    load_average_15m: float
    process_count: int
    uptime_seconds: int
    def __init__(self, collected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cpu_usage_percent: _Optional[float] = ..., memory_used_bytes: _Optional[int] = ..., memory_total_bytes: _Optional[int] = ..., disk_used_bytes: _Optional[int] = ..., disk_total_bytes: _Optional[int] = ..., network_bytes_received: _Optional[int] = ..., network_bytes_sent: _Optional[int] = ..., active_connections: _Optional[int] = ..., load_average_1m: _Optional[float] = ..., load_average_5m: _Optional[float] = ..., load_average_15m: _Optional[float] = ..., process_count: _Optional[int] = ..., uptime_seconds: _Optional[int] = ...) -> None: ...
