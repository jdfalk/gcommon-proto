from gcommon.v1.metrics import dry_run_result_pb2 as _dry_run_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeletionResult(_message.Message):
    __slots__ = ("provider_deleted", "data_deleted_bytes", "metrics_deleted", "data_points_deleted", "deleted_indices", "stopped_exports", "deleted_backups", "cleanup_strategy_used", "deletion_duration", "dry_run_result")
    PROVIDER_DELETED_FIELD_NUMBER: _ClassVar[int]
    DATA_DELETED_BYTES_FIELD_NUMBER: _ClassVar[int]
    METRICS_DELETED_FIELD_NUMBER: _ClassVar[int]
    DATA_POINTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    DELETED_INDICES_FIELD_NUMBER: _ClassVar[int]
    STOPPED_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    DELETED_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_STRATEGY_USED_FIELD_NUMBER: _ClassVar[int]
    DELETION_DURATION_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_RESULT_FIELD_NUMBER: _ClassVar[int]
    provider_deleted: bool
    data_deleted_bytes: int
    metrics_deleted: int
    data_points_deleted: int
    deleted_indices: _containers.RepeatedScalarFieldContainer[str]
    stopped_exports: _containers.RepeatedScalarFieldContainer[str]
    deleted_backups: _containers.RepeatedScalarFieldContainer[str]
    cleanup_strategy_used: str
    deletion_duration: str
    dry_run_result: _dry_run_result_pb2.DryRunResult
    def __init__(self, provider_deleted: bool = ..., data_deleted_bytes: _Optional[int] = ..., metrics_deleted: _Optional[int] = ..., data_points_deleted: _Optional[int] = ..., deleted_indices: _Optional[_Iterable[str]] = ..., stopped_exports: _Optional[_Iterable[str]] = ..., deleted_backups: _Optional[_Iterable[str]] = ..., cleanup_strategy_used: _Optional[str] = ..., deletion_duration: _Optional[str] = ..., dry_run_result: _Optional[_Union[_dry_run_result_pb2.DryRunResult, _Mapping]] = ...) -> None: ...
