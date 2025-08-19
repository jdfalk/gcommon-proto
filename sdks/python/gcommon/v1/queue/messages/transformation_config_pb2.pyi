from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TransformationConfig(_message.Message):
    __slots__ = ("enabled", "transformation_script", "script_language", "transform_on_ingress", "transform_on_egress", "timeout_ms", "max_memory_mb", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATION_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_ON_INGRESS_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_ON_EGRESS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    transformation_script: str
    script_language: str
    transform_on_ingress: bool
    transform_on_egress: bool
    timeout_ms: int
    max_memory_mb: int
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., transformation_script: _Optional[str] = ..., script_language: _Optional[str] = ..., transform_on_ingress: bool = ..., transform_on_egress: bool = ..., timeout_ms: _Optional[int] = ..., max_memory_mb: _Optional[int] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...
