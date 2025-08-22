from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionDetails(_message.Message):
    __slots__ = ("delivery_endpoint", "auth_token", "heartbeat_interval_ms", "keep_alive_timeout_ms", "ssl_enabled", "connection_metadata")
    class ConnectionMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DELIVERY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    SSL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_METADATA_FIELD_NUMBER: _ClassVar[int]
    delivery_endpoint: str
    auth_token: str
    heartbeat_interval_ms: int
    keep_alive_timeout_ms: int
    ssl_enabled: bool
    connection_metadata: _containers.ScalarMap[str, str]
    def __init__(self, delivery_endpoint: _Optional[str] = ..., auth_token: _Optional[str] = ..., heartbeat_interval_ms: _Optional[int] = ..., keep_alive_timeout_ms: _Optional[int] = ..., ssl_enabled: bool = ..., connection_metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
