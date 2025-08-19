from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.metrics.messages import backup_info_pb2 as _backup_info_pb2
from gcommon.v1.metrics.messages import deletion_result_pb2 as _deletion_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteProviderResponse(_message.Message):
    __slots__ = ("success", "error", "provider_id", "deleted_at", "deletion_result", "warnings", "backup_info", "scheduled_deletion")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETION_RESULT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DELETION_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    provider_id: str
    deleted_at: _timestamp_pb2.Timestamp
    deletion_result: _deletion_result_pb2.DeletionResult
    warnings: _containers.RepeatedScalarFieldContainer[str]
    backup_info: _backup_info_pb2.MetricsBackupInfo
    scheduled_deletion: _timestamp_pb2.Timestamp
    def __init__(self, success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., provider_id: _Optional[str] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deletion_result: _Optional[_Union[_deletion_result_pb2.DeletionResult, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ..., backup_info: _Optional[_Union[_backup_info_pb2.MetricsBackupInfo, _Mapping]] = ..., scheduled_deletion: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
