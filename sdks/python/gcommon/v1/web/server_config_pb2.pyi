from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerConfig(_message.Message):
    __slots__ = ("host", "port", "enable_tls", "tls_cert_path", "tls_key_path", "trusted_proxies", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TLS_FIELD_NUMBER: _ClassVar[int]
    TLS_CERT_PATH_FIELD_NUMBER: _ClassVar[int]
    TLS_KEY_PATH_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_PROXIES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    enable_tls: bool
    tls_cert_path: str
    tls_key_path: str
    trusted_proxies: _containers.RepeatedScalarFieldContainer[str]
    options: _containers.ScalarMap[str, str]
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ..., enable_tls: _Optional[bool] = ..., tls_cert_path: _Optional[str] = ..., tls_key_path: _Optional[str] = ..., trusted_proxies: _Optional[_Iterable[str]] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...
