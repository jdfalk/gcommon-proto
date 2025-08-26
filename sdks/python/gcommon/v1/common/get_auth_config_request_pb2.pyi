from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetAuthConfigRequest(_message.Message):
    __slots__ = ("keys", "include_sensitive")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    include_sensitive: bool
    def __init__(self, keys: _Optional[_Iterable[str]] = ..., include_sensitive: _Optional[bool] = ...) -> None: ...
