from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalRoleProvider(_message.Message):
    __slots__ = ("provider_type", "endpoint", "credentials", "cache_ttl_seconds")
    class CredentialsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    CACHE_TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    provider_type: str
    endpoint: str
    credentials: _containers.ScalarMap[str, str]
    cache_ttl_seconds: int
    def __init__(
        self,
        provider_type: _Optional[str] = ...,
        endpoint: _Optional[str] = ...,
        credentials: _Optional[_Mapping[str, str]] = ...,
        cache_ttl_seconds: _Optional[int] = ...,
    ) -> None: ...
