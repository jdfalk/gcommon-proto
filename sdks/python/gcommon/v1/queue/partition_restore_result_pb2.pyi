import datetime

from gcommon.v1.queue import restore_error_pb2 as _restore_error_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartitionRestoreResult(_message.Message):
    __slots__ = ("partition_id", "success", "messages_restored", "bytes_restored", "start_offset", "end_offset", "restore_duration", "partition_errors", "partition_metadata")
    class PartitionMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    BYTES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DURATION_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_METADATA_FIELD_NUMBER: _ClassVar[int]
    partition_id: int
    success: bool
    messages_restored: int
    bytes_restored: int
    start_offset: int
    end_offset: int
    restore_duration: _duration_pb2.Duration
    partition_errors: _containers.RepeatedCompositeFieldContainer[_restore_error_pb2.RestoreError]
    partition_metadata: _containers.ScalarMap[str, str]
    def __init__(self, partition_id: _Optional[int] = ..., success: _Optional[bool] = ..., messages_restored: _Optional[int] = ..., bytes_restored: _Optional[int] = ..., start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ..., restore_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., partition_errors: _Optional[_Iterable[_Union[_restore_error_pb2.RestoreError, _Mapping]]] = ..., partition_metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
