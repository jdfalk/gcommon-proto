from gcommon.v1.database import cache_entry_pb2 as _cache_entry_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetResponse(_message.Message):
    __slots__ = ("entry", "found", "cache_hit")
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    CACHE_HIT_FIELD_NUMBER: _ClassVar[int]
    entry: _cache_entry_pb2.CacheEntry
    found: bool
    cache_hit: bool
    def __init__(
        self,
        entry: _Optional[_Union[_cache_entry_pb2.CacheEntry, _Mapping]] = ...,
        found: _Optional[bool] = ...,
        cache_hit: _Optional[bool] = ...,
    ) -> None: ...
