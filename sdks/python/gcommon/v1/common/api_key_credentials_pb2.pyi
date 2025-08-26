from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class APIKeyCredentials(_message.Message):
    __slots__ = ("key", "key_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    key: str
    key_id: str
    def __init__(self, key: _Optional[str] = ..., key_id: _Optional[str] = ...) -> None: ...
