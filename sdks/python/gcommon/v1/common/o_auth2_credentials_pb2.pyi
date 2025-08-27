from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OAuth2Credentials(_message.Message):
    __slots__ = ("code", "redirect_uri", "client_id", "client_secret")
    CODE_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    code: str
    redirect_uri: str
    client_id: str
    client_secret: str
    def __init__(
        self,
        code: _Optional[str] = ...,
        redirect_uri: _Optional[str] = ...,
        client_id: _Optional[str] = ...,
        client_secret: _Optional[str] = ...,
    ) -> None: ...
