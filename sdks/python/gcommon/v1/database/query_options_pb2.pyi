from gcommon.v1.database import consistency_level_pb2 as _consistency_level_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryOptions(_message.Message):
    __slots__ = ("limit", "offset", "timeout", "include_metadata", "consistency")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    timeout: _duration_pb2.Duration
    include_metadata: bool
    consistency: _consistency_level_pb2.DatabaseConsistencyLevel
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., include_metadata: bool = ..., consistency: _Optional[_Union[_consistency_level_pb2.DatabaseConsistencyLevel, str]] = ...) -> None: ...
