from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StoragePolicy(_message.Message):
    __slots__ = ("name", "statement", "effect", "resources", "actions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    statement: str
    effect: str
    resources: _containers.RepeatedScalarFieldContainer[str]
    actions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., statement: _Optional[str] = ..., effect: _Optional[str] = ..., resources: _Optional[_Iterable[str]] = ..., actions: _Optional[_Iterable[str]] = ...) -> None: ...
