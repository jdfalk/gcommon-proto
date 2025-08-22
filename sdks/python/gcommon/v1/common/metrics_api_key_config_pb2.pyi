from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsAPIKeyConfig(_message.Message):
    __slots__ = ("header_name", "required", "allowed_keys")
    HEADER_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_KEYS_FIELD_NUMBER: _ClassVar[int]
    header_name: str
    required: bool
    allowed_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header_name: _Optional[str] = ..., required: bool = ..., allowed_keys: _Optional[_Iterable[str]] = ...) -> None: ...
