import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthRateLimitConfig(_message.Message):
    __slots__ = ("max_requests", "time_window", "burst_allowance", "scope", "action", "enabled", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MAX_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
    BURST_ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    max_requests: int
    time_window: _duration_pb2.Duration
    burst_allowance: int
    scope: str
    action: str
    enabled: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, max_requests: _Optional[int] = ..., time_window: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., burst_allowance: _Optional[int] = ..., scope: _Optional[str] = ..., action: _Optional[str] = ..., enabled: _Optional[bool] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
