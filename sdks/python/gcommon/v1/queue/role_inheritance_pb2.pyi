from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RoleInheritance(_message.Message):
    __slots__ = ("inherits_from", "additional_permissions")
    INHERITS_FROM_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    inherits_from: _containers.RepeatedScalarFieldContainer[str]
    additional_permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, inherits_from: _Optional[_Iterable[str]] = ..., additional_permissions: _Optional[_Iterable[str]] = ...) -> None: ...
