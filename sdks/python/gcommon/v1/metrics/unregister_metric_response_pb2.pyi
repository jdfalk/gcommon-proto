import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import backup_info_pb2 as _backup_info_pb2
from gcommon.v1.metrics import unregistration_result_pb2 as _unregistration_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnregisterMetricResponse(_message.Message):
    __slots__ = (
        "success",
        "error",
        "metric_id",
        "metric_name",
        "unregistered_at",
        "provider_id",
        "result",
        "warnings",
        "backup_info",
    )
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    UNREGISTERED_AT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    metric_id: str
    metric_name: str
    unregistered_at: _timestamp_pb2.Timestamp
    provider_id: str
    result: _unregistration_result_pb2.UnregistrationResult
    warnings: _containers.RepeatedScalarFieldContainer[str]
    backup_info: _backup_info_pb2.MetricsBackupInfo
    def __init__(
        self,
        success: _Optional[bool] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        metric_id: _Optional[str] = ...,
        metric_name: _Optional[str] = ...,
        unregistered_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        provider_id: _Optional[str] = ...,
        result: _Optional[
            _Union[_unregistration_result_pb2.UnregistrationResult, _Mapping]
        ] = ...,
        warnings: _Optional[_Iterable[str]] = ...,
        backup_info: _Optional[
            _Union[_backup_info_pb2.MetricsBackupInfo, _Mapping]
        ] = ...,
    ) -> None: ...
