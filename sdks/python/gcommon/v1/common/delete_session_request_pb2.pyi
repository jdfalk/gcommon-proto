from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthDeleteSessionRequest(_message.Message):
    __slots__ = ("session_id", "force")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    force: bool
    def __init__(
        self, session_id: _Optional[str] = ..., force: _Optional[bool] = ...
    ) -> None: ...
