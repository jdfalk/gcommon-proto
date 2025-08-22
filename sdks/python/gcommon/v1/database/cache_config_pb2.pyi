from gcommon.v1.common import eviction_policy_pb2 as _eviction_policy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheCacheConfig(_message.Message):
    __slots__ = ("max_entries", "max_memory_bytes", "default_ttl", "eviction_policy", "enable_stats", "enable_persistence", "persistence_file", "name")
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TTL_FIELD_NUMBER: _ClassVar[int]
    EVICTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STATS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PERSISTENCE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_FILE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    max_entries: int
    max_memory_bytes: int
    default_ttl: _duration_pb2.Duration
    eviction_policy: _eviction_policy_pb2.EvictionPolicy
    enable_stats: bool
    enable_persistence: bool
    persistence_file: str
    name: str
    def __init__(self, max_entries: _Optional[int] = ..., max_memory_bytes: _Optional[int] = ..., default_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., eviction_policy: _Optional[_Union[_eviction_policy_pb2.EvictionPolicy, str]] = ..., enable_stats: bool = ..., enable_persistence: bool = ..., persistence_file: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
