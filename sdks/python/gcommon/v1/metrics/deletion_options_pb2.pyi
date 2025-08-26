from gcommon.v1.common import cleanup_strategy_pb2 as _cleanup_strategy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeletionOptions(_message.Message):
    __slots__ = ("delete_data", "delete_indices", "delete_backups", "stop_exports", "grace_period", "dry_run", "force", "create_backup", "cleanup_strategy", "wait_for_completion", "completion_timeout")
    DELETE_DATA_FIELD_NUMBER: _ClassVar[int]
    DELETE_INDICES_FIELD_NUMBER: _ClassVar[int]
    DELETE_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    STOP_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    GRACE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    delete_data: bool
    delete_indices: bool
    delete_backups: bool
    stop_exports: bool
    grace_period: str
    dry_run: bool
    force: bool
    create_backup: bool
    cleanup_strategy: _cleanup_strategy_pb2.CleanupStrategy
    wait_for_completion: bool
    completion_timeout: str
    def __init__(self, delete_data: _Optional[bool] = ..., delete_indices: _Optional[bool] = ..., delete_backups: _Optional[bool] = ..., stop_exports: _Optional[bool] = ..., grace_period: _Optional[str] = ..., dry_run: _Optional[bool] = ..., force: _Optional[bool] = ..., create_backup: _Optional[bool] = ..., cleanup_strategy: _Optional[_Union[_cleanup_strategy_pb2.CleanupStrategy, str]] = ..., wait_for_completion: _Optional[bool] = ..., completion_timeout: _Optional[str] = ...) -> None: ...
