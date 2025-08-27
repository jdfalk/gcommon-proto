from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WebTLSConfig(_message.Message):
    __slots__ = (
        "cert_file",
        "key_file",
        "ca_file",
        "min_version",
        "max_version",
        "cipher_suites",
        "require_client_cert",
        "verify_client_cert",
        "server_name",
    )
    CERT_FILE_FIELD_NUMBER: _ClassVar[int]
    KEY_FILE_FIELD_NUMBER: _ClassVar[int]
    CA_FILE_FIELD_NUMBER: _ClassVar[int]
    MIN_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAX_VERSION_FIELD_NUMBER: _ClassVar[int]
    CIPHER_SUITES_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_CLIENT_CERT_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CLIENT_CERT_FIELD_NUMBER: _ClassVar[int]
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    cert_file: str
    key_file: str
    ca_file: str
    min_version: str
    max_version: str
    cipher_suites: _containers.RepeatedScalarFieldContainer[str]
    require_client_cert: bool
    verify_client_cert: bool
    server_name: str
    def __init__(
        self,
        cert_file: _Optional[str] = ...,
        key_file: _Optional[str] = ...,
        ca_file: _Optional[str] = ...,
        min_version: _Optional[str] = ...,
        max_version: _Optional[str] = ...,
        cipher_suites: _Optional[_Iterable[str]] = ...,
        require_client_cert: _Optional[bool] = ...,
        verify_client_cert: _Optional[bool] = ...,
        server_name: _Optional[str] = ...,
    ) -> None: ...
