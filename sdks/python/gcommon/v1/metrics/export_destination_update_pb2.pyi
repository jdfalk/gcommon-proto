from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExportDestinationUpdate(_message.Message):
    __slots__ = ("destination_id", "url", "auth_token", "enabled")
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    destination_id: str
    url: str
    auth_token: str
    enabled: bool
    def __init__(self, destination_id: _Optional[str] = ..., url: _Optional[str] = ..., auth_token: _Optional[str] = ..., enabled: bool = ...) -> None: ...
