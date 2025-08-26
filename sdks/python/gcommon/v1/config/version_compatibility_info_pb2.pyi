from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VersionCompatibilityInfo(_message.Message):
    __slots__ = ("backward_compatible", "forward_compatible", "breaking_changes", "notes", "min_version", "max_version", "deprecated_features", "migration_guide")
    BACKWARD_COMPATIBLE_FIELD_NUMBER: _ClassVar[int]
    FORWARD_COMPATIBLE_FIELD_NUMBER: _ClassVar[int]
    BREAKING_CHANGES_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    MIN_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAX_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_GUIDE_FIELD_NUMBER: _ClassVar[int]
    backward_compatible: bool
    forward_compatible: bool
    breaking_changes: _containers.RepeatedScalarFieldContainer[str]
    notes: str
    min_version: str
    max_version: str
    deprecated_features: _containers.RepeatedScalarFieldContainer[str]
    migration_guide: str
    def __init__(self, backward_compatible: _Optional[bool] = ..., forward_compatible: _Optional[bool] = ..., breaking_changes: _Optional[_Iterable[str]] = ..., notes: _Optional[str] = ..., min_version: _Optional[str] = ..., max_version: _Optional[str] = ..., deprecated_features: _Optional[_Iterable[str]] = ..., migration_guide: _Optional[str] = ...) -> None: ...
