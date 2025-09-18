import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckConfig(_message.Message):
    __slots__ = ("default_interval", "default_timeout", "default_failure_threshold", "default_success_threshold", "enable_metrics", "enable_logging", "max_concurrent_checks", "global_tags", "retention_period", "auto_retry")
    DEFAULT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SUCCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_METRICS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LOGGING_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_CHECKS_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TAGS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    AUTO_RETRY_FIELD_NUMBER: _ClassVar[int]
    default_interval: _duration_pb2.Duration
    default_timeout: _duration_pb2.Duration
    default_failure_threshold: int
    default_success_threshold: int
    enable_metrics: bool
    enable_logging: bool
    max_concurrent_checks: int
    global_tags: _containers.RepeatedScalarFieldContainer[str]
    retention_period: _duration_pb2.Duration
    auto_retry: bool
    def __init__(self, default_interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., default_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., default_failure_threshold: _Optional[int] = ..., default_success_threshold: _Optional[int] = ..., enable_metrics: _Optional[bool] = ..., enable_logging: _Optional[bool] = ..., max_concurrent_checks: _Optional[int] = ..., global_tags: _Optional[_Iterable[str]] = ..., retention_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., auto_retry: _Optional[bool] = ...) -> None: ...
