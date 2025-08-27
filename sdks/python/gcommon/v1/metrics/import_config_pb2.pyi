from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImportConfig(_message.Message):
    __slots__ = ("sources", "schedule", "enabled")
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedScalarFieldContainer[str]
    schedule: str
    enabled: bool
    def __init__(self, sources: _Optional[_Iterable[str]] = ..., schedule: _Optional[str] = ..., enabled: _Optional[bool] = ...) -> None: ...
