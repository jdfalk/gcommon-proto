from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TLSConfigUpdate(_message.Message):
    __slots__ = ("cert_file", "key_file", "ca_file", "verify_certs")
    CERT_FILE_FIELD_NUMBER: _ClassVar[int]
    KEY_FILE_FIELD_NUMBER: _ClassVar[int]
    CA_FILE_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CERTS_FIELD_NUMBER: _ClassVar[int]
    cert_file: str
    key_file: str
    ca_file: str
    verify_certs: bool
    def __init__(self, cert_file: _Optional[str] = ..., key_file: _Optional[str] = ..., ca_file: _Optional[str] = ..., verify_certs: bool = ...) -> None: ...
