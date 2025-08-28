from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigResourceLimits(_message.Message):
    __slots__ = ("cpu_limit", "memory_limit", "storage_limit", "network_limit", "request_rate_limit", "connection_limit", "custom_limits")
    class CustomLimitsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_LIMIT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_RATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LIMITS_FIELD_NUMBER: _ClassVar[int]
    cpu_limit: str
    memory_limit: str
    storage_limit: str
    network_limit: str
    request_rate_limit: int
    connection_limit: int
    custom_limits: _containers.ScalarMap[str, str]
    def __init__(self, cpu_limit: _Optional[str] = ..., memory_limit: _Optional[str] = ..., storage_limit: _Optional[str] = ..., network_limit: _Optional[str] = ..., request_rate_limit: _Optional[int] = ..., connection_limit: _Optional[int] = ..., custom_limits: _Optional[_Mapping[str, str]] = ...) -> None: ...
