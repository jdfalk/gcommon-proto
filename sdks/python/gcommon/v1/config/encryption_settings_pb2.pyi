from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EncryptionSettings(_message.Message):
    __slots__ = ("enabled", "provider", "key_id", "algorithm", "mode", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    provider: str
    key_id: str
    algorithm: str
    mode: str
    config: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., provider: _Optional[str] = ..., key_id: _Optional[str] = ..., algorithm: _Optional[str] = ..., mode: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...
