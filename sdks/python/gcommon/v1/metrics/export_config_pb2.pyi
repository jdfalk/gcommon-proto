from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportConfig(_message.Message):
    __slots__ = ("destination", "format", "frequency_seconds", "compress", "batch_size", "timeout_seconds", "headers", "auth_config", "retry_config", "include_patterns", "exclude_patterns")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AuthConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    COMPRESS_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    destination: str
    format: str
    frequency_seconds: int
    compress: bool
    batch_size: int
    timeout_seconds: int
    headers: _containers.ScalarMap[str, str]
    auth_config: _containers.ScalarMap[str, str]
    retry_config: MetricsRetryConfig
    include_patterns: _containers.RepeatedScalarFieldContainer[str]
    exclude_patterns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, destination: _Optional[str] = ..., format: _Optional[str] = ..., frequency_seconds: _Optional[int] = ..., compress: bool = ..., batch_size: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., headers: _Optional[_Mapping[str, str]] = ..., auth_config: _Optional[_Mapping[str, str]] = ..., retry_config: _Optional[_Union[MetricsRetryConfig, _Mapping]] = ..., include_patterns: _Optional[_Iterable[str]] = ..., exclude_patterns: _Optional[_Iterable[str]] = ...) -> None: ...

class MetricsRetryConfig(_message.Message):
    __slots__ = ("max_retries", "initial_delay_seconds", "max_delay_seconds", "backoff_multiplier")
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    max_retries: int
    initial_delay_seconds: int
    max_delay_seconds: int
    backoff_multiplier: float
    def __init__(self, max_retries: _Optional[int] = ..., initial_delay_seconds: _Optional[int] = ..., max_delay_seconds: _Optional[int] = ..., backoff_multiplier: _Optional[float] = ...) -> None: ...
