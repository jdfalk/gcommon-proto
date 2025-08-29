from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.metrics import metrics_retry_config_pb2 as _metrics_retry_config_pb2
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
    retry_config: _metrics_retry_config_pb2.MetricsRetryConfig
    include_patterns: _containers.RepeatedScalarFieldContainer[str]
    exclude_patterns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, destination: _Optional[str] = ..., format: _Optional[str] = ..., frequency_seconds: _Optional[int] = ..., compress: bool = ..., batch_size: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., headers: _Optional[_Mapping[str, str]] = ..., auth_config: _Optional[_Mapping[str, str]] = ..., retry_config: _Optional[_Union[_metrics_retry_config_pb2.MetricsRetryConfig, _Mapping]] = ..., include_patterns: _Optional[_Iterable[str]] = ..., exclude_patterns: _Optional[_Iterable[str]] = ...) -> None: ...
