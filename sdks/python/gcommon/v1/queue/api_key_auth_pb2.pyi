from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class APIKeyAuth(_message.Message):
    __slots__ = ("api_key", "key_id")
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    key_id: str
    def __init__(
        self, api_key: _Optional[str] = ..., key_id: _Optional[str] = ...
    ) -> None: ...
