from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StorageEncryption(_message.Message):
    __slots__ = ("type", "key_id", "server_side", "client_side")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_SIDE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SIDE_FIELD_NUMBER: _ClassVar[int]
    type: str
    key_id: str
    server_side: bool
    client_side: bool
    def __init__(self, type: _Optional[str] = ..., key_id: _Optional[str] = ..., server_side: bool = ..., client_side: bool = ...) -> None: ...
