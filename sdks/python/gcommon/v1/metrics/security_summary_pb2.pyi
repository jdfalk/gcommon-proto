from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SecuritySummary(_message.Message):
    __slots__ = ("auth_enabled", "tls_enabled", "auth_methods")
    AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTH_METHODS_FIELD_NUMBER: _ClassVar[int]
    auth_enabled: bool
    tls_enabled: bool
    auth_methods: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, auth_enabled: bool = ..., tls_enabled: bool = ..., auth_methods: _Optional[_Iterable[str]] = ...) -> None: ...
