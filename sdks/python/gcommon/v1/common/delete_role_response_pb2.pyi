from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteRoleResponse(_message.Message):
    __slots__ = ("success", "error_message", "affected_subjects")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    affected_subjects: int
    def __init__(self, success: _Optional[bool] = ..., error_message: _Optional[str] = ..., affected_subjects: _Optional[int] = ...) -> None: ...
