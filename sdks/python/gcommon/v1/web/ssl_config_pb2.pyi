from gcommon.v1.web import ssl_protocol_pb2 as _ssl_protocol_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SslConfig(_message.Message):
    __slots__ = ("protocol", "cert_file", "key_file", "ca_file", "require_client_auth")
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    CERT_FILE_FIELD_NUMBER: _ClassVar[int]
    KEY_FILE_FIELD_NUMBER: _ClassVar[int]
    CA_FILE_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_CLIENT_AUTH_FIELD_NUMBER: _ClassVar[int]
    protocol: _ssl_protocol_pb2.SSLProtocol
    cert_file: str
    key_file: str
    ca_file: str
    require_client_auth: bool
    def __init__(self, protocol: _Optional[_Union[_ssl_protocol_pb2.SSLProtocol, str]] = ..., cert_file: _Optional[str] = ..., key_file: _Optional[str] = ..., ca_file: _Optional[str] = ..., require_client_auth: bool = ...) -> None: ...
