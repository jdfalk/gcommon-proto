from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionRule(_message.Message):
    __slots__ = ("resource_pattern", "operation", "required_roles", "allow", "priority")
    RESOURCE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ROLES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    resource_pattern: str
    operation: str
    required_roles: _containers.RepeatedScalarFieldContainer[str]
    allow: bool
    priority: int
    def __init__(
        self,
        resource_pattern: _Optional[str] = ...,
        operation: _Optional[str] = ...,
        required_roles: _Optional[_Iterable[str]] = ...,
        allow: _Optional[bool] = ...,
        priority: _Optional[int] = ...,
    ) -> None: ...
