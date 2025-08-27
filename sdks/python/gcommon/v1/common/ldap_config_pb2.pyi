from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LdapConfig(_message.Message):
    __slots__ = ("host", "port", "use_tls", "bind_dn", "bind_password", "base_dn", "user_filter", "group_filter", "timeout_seconds", "attributes")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USE_TLS_FIELD_NUMBER: _ClassVar[int]
    BIND_DN_FIELD_NUMBER: _ClassVar[int]
    BIND_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    BASE_DN_FIELD_NUMBER: _ClassVar[int]
    USER_FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_FILTER_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    use_tls: bool
    bind_dn: str
    bind_password: str
    base_dn: str
    user_filter: str
    group_filter: str
    timeout_seconds: int
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ..., use_tls: _Optional[bool] = ..., bind_dn: _Optional[str] = ..., bind_password: _Optional[str] = ..., base_dn: _Optional[str] = ..., user_filter: _Optional[str] = ..., group_filter: _Optional[str] = ..., timeout_seconds: _Optional[int] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...
