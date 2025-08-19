from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SSLConfig(_message.Message):
    __slots__ = ("certificate_id", "ssl_policy", "redirect_http", "min_tls_version")
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    SSL_POLICY_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_HTTP_FIELD_NUMBER: _ClassVar[int]
    MIN_TLS_VERSION_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    ssl_policy: str
    redirect_http: bool
    min_tls_version: str
    def __init__(self, certificate_id: _Optional[str] = ..., ssl_policy: _Optional[str] = ..., redirect_http: bool = ..., min_tls_version: _Optional[str] = ...) -> None: ...
