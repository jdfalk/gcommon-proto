from gcommon.v1.queue.messages import backup_info_pb2 as _backup_info_pb2
from gcommon.v1.queue.messages import deletion_stats_pb2 as _deletion_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueDeleteResponse(_message.Message):
    __slots__ = ("success", "deleted_resource_id", "resource_type", "deleted_at", "error_message", "error_code", "deletion_stats", "backup_info", "warnings", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DELETED_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    DELETION_STATS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    deleted_resource_id: str
    resource_type: str
    deleted_at: _timestamp_pb2.Timestamp
    error_message: str
    error_code: str
    deletion_stats: _deletion_stats_pb2.DeletionStats
    backup_info: _backup_info_pb2.QueueBackupInfo
    warnings: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, success: bool = ..., deleted_resource_id: _Optional[str] = ..., resource_type: _Optional[str] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error_message: _Optional[str] = ..., error_code: _Optional[str] = ..., deletion_stats: _Optional[_Union[_deletion_stats_pb2.DeletionStats, _Mapping]] = ..., backup_info: _Optional[_Union[_backup_info_pb2.QueueBackupInfo, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
