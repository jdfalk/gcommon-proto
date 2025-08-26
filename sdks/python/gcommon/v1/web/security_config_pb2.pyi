from gcommon.v1.web import tls_config_pb2 as _tls_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebSecurityConfig(_message.Message):
    __slots__ = ("enable_tls", "tls", "allowed_hosts", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLE_TLS_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_HOSTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    enable_tls: bool
    tls: _tls_config_pb2.WebTLSConfig
    allowed_hosts: _containers.RepeatedScalarFieldContainer[str]
    options: _containers.ScalarMap[str, str]
    def __init__(self, enable_tls: bool = ..., tls: _Optional[_Union[_tls_config_pb2.WebTLSConfig, _Mapping]] = ..., allowed_hosts: _Optional[_Iterable[str]] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...
