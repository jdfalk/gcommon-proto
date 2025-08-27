from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KeyValidationService(_message.Message):
    __slots__ = ("service_type", "endpoint", "timeout_ms", "cache_ttl_seconds")
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    CACHE_TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    service_type: str
    endpoint: str
    timeout_ms: int
    cache_ttl_seconds: int
    def __init__(
        self,
        service_type: _Optional[str] = ...,
        endpoint: _Optional[str] = ...,
        timeout_ms: _Optional[int] = ...,
        cache_ttl_seconds: _Optional[int] = ...,
    ) -> None: ...
