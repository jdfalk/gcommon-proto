import datetime

from gcommon.v1.common import eviction_policy_pb2 as _eviction_policy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvictionResult(_message.Message):
    __slots__ = ("evicted_count", "evicted_keys", "policy_used", "eviction_reason", "evicted_at", "memory_freed", "success")
    EVICTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    EVICTED_KEYS_FIELD_NUMBER: _ClassVar[int]
    POLICY_USED_FIELD_NUMBER: _ClassVar[int]
    EVICTION_REASON_FIELD_NUMBER: _ClassVar[int]
    EVICTED_AT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FREED_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    evicted_count: int
    evicted_keys: _containers.RepeatedScalarFieldContainer[str]
    policy_used: _eviction_policy_pb2.EvictionPolicy
    eviction_reason: str
    evicted_at: _timestamp_pb2.Timestamp
    memory_freed: int
    success: bool
    def __init__(self, evicted_count: _Optional[int] = ..., evicted_keys: _Optional[_Iterable[str]] = ..., policy_used: _Optional[_Union[_eviction_policy_pb2.EvictionPolicy, str]] = ..., eviction_reason: _Optional[str] = ..., evicted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., memory_freed: _Optional[int] = ..., success: _Optional[bool] = ...) -> None: ...
