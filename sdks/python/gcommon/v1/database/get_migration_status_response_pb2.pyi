from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetMigrationStatusResponse(_message.Message):
    __slots__ = ("current_version", "applied_versions", "pending_versions")
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    APPLIED_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    PENDING_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    current_version: str
    applied_versions: _containers.RepeatedScalarFieldContainer[str]
    pending_versions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        current_version: _Optional[str] = ...,
        applied_versions: _Optional[_Iterable[str]] = ...,
        pending_versions: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
