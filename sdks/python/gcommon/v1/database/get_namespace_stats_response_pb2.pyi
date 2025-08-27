import datetime

from gcommon.v1.database import namespace_stats_pb2 as _namespace_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetNamespaceStatsResponse(_message.Message):
    __slots__ = ("namespace_id", "stats", "collected_at")
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    COLLECTED_AT_FIELD_NUMBER: _ClassVar[int]
    namespace_id: str
    stats: _namespace_stats_pb2.NamespaceStats
    collected_at: _timestamp_pb2.Timestamp
    def __init__(self, namespace_id: _Optional[str] = ..., stats: _Optional[_Union[_namespace_stats_pb2.NamespaceStats, _Mapping]] = ..., collected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
