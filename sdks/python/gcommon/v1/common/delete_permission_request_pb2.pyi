from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeletePermissionRequest(_message.Message):
    __slots__ = ("permission_id", "force")
    PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    permission_id: str
    force: bool
    def __init__(self, permission_id: _Optional[str] = ..., force: _Optional[bool] = ...) -> None: ...
