from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NodeStats(_message.Message):
    __slots__ = ("queue_count", "message_count", "cpu_usage", "memory_usage", "disk_usage", "network_throughput")
    QUEUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    DISK_USAGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    queue_count: int
    message_count: int
    cpu_usage: float
    memory_usage: int
    disk_usage: int
    network_throughput: float
    def __init__(self, queue_count: _Optional[int] = ..., message_count: _Optional[int] = ..., cpu_usage: _Optional[float] = ..., memory_usage: _Optional[int] = ..., disk_usage: _Optional[int] = ..., network_throughput: _Optional[float] = ...) -> None: ...
