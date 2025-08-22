from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteNamespaceRequest(_message.Message):
    __slots__ = ("namespace_id", "force", "backup")
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    namespace_id: str
    force: bool
    backup: bool
    def __init__(self, namespace_id: _Optional[str] = ..., force: bool = ..., backup: bool = ...) -> None: ...
