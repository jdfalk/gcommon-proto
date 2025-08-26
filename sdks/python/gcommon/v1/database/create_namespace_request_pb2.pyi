from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNamespaceRequest(_message.Message):
    __slots__ = ("name", "description", "max_keys", "max_memory_bytes", "default_ttl_seconds", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MAX_KEYS_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    max_keys: int
    max_memory_bytes: int
    default_ttl_seconds: int
    config: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., max_keys: _Optional[int] = ..., max_memory_bytes: _Optional[int] = ..., default_ttl_seconds: _Optional[int] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...
