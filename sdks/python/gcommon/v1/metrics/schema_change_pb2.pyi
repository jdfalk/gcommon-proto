from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SchemaChange(_message.Message):
    __slots__ = ("change_type", "description", "backward_compatible", "migration_steps")
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKWARD_COMPATIBLE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_STEPS_FIELD_NUMBER: _ClassVar[int]
    change_type: str
    description: str
    backward_compatible: bool
    migration_steps: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, change_type: _Optional[str] = ..., description: _Optional[str] = ..., backward_compatible: _Optional[bool] = ..., migration_steps: _Optional[_Iterable[str]] = ...) -> None: ...
