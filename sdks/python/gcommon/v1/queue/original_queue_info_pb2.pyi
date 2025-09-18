import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OriginalQueueInfo(_message.Message):
    __slots__ = ("queue_id", "queue_name", "partition_count", "config_snapshot", "backup_point")
    class ConfigSnapshotEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_POINT_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    queue_name: str
    partition_count: int
    config_snapshot: _containers.ScalarMap[str, str]
    backup_point: _timestamp_pb2.Timestamp
    def __init__(self, queue_id: _Optional[str] = ..., queue_name: _Optional[str] = ..., partition_count: _Optional[int] = ..., config_snapshot: _Optional[_Mapping[str, str]] = ..., backup_point: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
