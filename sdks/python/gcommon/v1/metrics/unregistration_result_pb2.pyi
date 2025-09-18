import datetime

from gcommon.v1.metrics import dry_run_result_pb2 as _dry_run_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnregistrationResult(_message.Message):
    __slots__ = ("definition_deleted", "data_deleted_bytes", "data_points_deleted", "deleted_indices", "removed_alerts", "stopped_exports", "scheduled_deletion", "dry_run_result")
    DEFINITION_DELETED_FIELD_NUMBER: _ClassVar[int]
    DATA_DELETED_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_POINTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    DELETED_INDICES_FIELD_NUMBER: _ClassVar[int]
    REMOVED_ALERTS_FIELD_NUMBER: _ClassVar[int]
    STOPPED_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DELETION_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_RESULT_FIELD_NUMBER: _ClassVar[int]
    definition_deleted: bool
    data_deleted_bytes: int
    data_points_deleted: int
    deleted_indices: _containers.RepeatedScalarFieldContainer[str]
    removed_alerts: _containers.RepeatedScalarFieldContainer[str]
    stopped_exports: _containers.RepeatedScalarFieldContainer[str]
    scheduled_deletion: _timestamp_pb2.Timestamp
    dry_run_result: _dry_run_result_pb2.DryRunResult
    def __init__(self, definition_deleted: _Optional[bool] = ..., data_deleted_bytes: _Optional[int] = ..., data_points_deleted: _Optional[int] = ..., deleted_indices: _Optional[_Iterable[str]] = ..., removed_alerts: _Optional[_Iterable[str]] = ..., stopped_exports: _Optional[_Iterable[str]] = ..., scheduled_deletion: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dry_run_result: _Optional[_Union[_dry_run_result_pb2.DryRunResult, _Mapping]] = ...) -> None: ...
