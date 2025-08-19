from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NamespaceInfo(_message.Message):
    __slots__ = ("namespace_id", "name", "description", "created_at", "current_keys", "current_memory_bytes", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_KEYS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    namespace_id: str
    name: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    current_keys: int
    current_memory_bytes: int
    config: _containers.ScalarMap[str, str]
    def __init__(self, namespace_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., current_keys: _Optional[int] = ..., current_memory_bytes: _Optional[int] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...
