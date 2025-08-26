from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateQueueResponse(_message.Message):
    __slots__ = ("success", "queue_name", "queue_endpoint", "partition_count", "applied_config", "error")
    class AppliedConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    queue_name: str
    queue_endpoint: str
    partition_count: int
    applied_config: _containers.ScalarMap[str, str]
    error: str
    def __init__(self, success: _Optional[bool] = ..., queue_name: _Optional[str] = ..., queue_endpoint: _Optional[str] = ..., partition_count: _Optional[int] = ..., applied_config: _Optional[_Mapping[str, str]] = ..., error: _Optional[str] = ...) -> None: ...
