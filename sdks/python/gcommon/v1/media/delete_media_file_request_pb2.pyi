from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteMediaFileRequest(_message.Message):
    __slots__ = ("id", "delete_from_storage")
    ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_FROM_STORAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    delete_from_storage: bool
    def __init__(
        self, id: _Optional[str] = ..., delete_from_storage: _Optional[bool] = ...
    ) -> None: ...
