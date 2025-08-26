from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TLSAuth(_message.Message):
    __slots__ = ("cert_pem", "key_pem", "ca_pem", "verify_server")
    CERT_PEM_FIELD_NUMBER: _ClassVar[int]
    KEY_PEM_FIELD_NUMBER: _ClassVar[int]
    CA_PEM_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SERVER_FIELD_NUMBER: _ClassVar[int]
    cert_pem: str
    key_pem: str
    ca_pem: str
    verify_server: bool
    def __init__(self, cert_pem: _Optional[str] = ..., key_pem: _Optional[str] = ..., ca_pem: _Optional[str] = ..., verify_server: _Optional[bool] = ...) -> None: ...
