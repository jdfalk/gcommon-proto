from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigValidationWarning(_message.Message):
    __slots__ = ("key", "message", "code")
    KEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    key: str
    message: str
    code: str
    def __init__(self, key: _Optional[str] = ..., message: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...
