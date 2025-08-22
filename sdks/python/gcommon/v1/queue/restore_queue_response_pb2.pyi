from gcommon.v1.metrics import validation_result_pb2 as _validation_result_pb2
from gcommon.v1.queue import partition_restore_result_pb2 as _partition_restore_result_pb2
from gcommon.v1.queue import restore_error_pb2 as _restore_error_pb2
from gcommon.v1.queue import restore_statistics_pb2 as _restore_statistics_pb2
from gcommon.v1.queue import restore_status_pb2 as _restore_status_pb2
from gcommon.v1.queue import restore_warning_pb2 as _restore_warning_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreQueueResponse(_message.Message):
    __slots__ = ("success", "operation_id", "restored_queue_id", "start_time", "completion_time", "duration", "statistics", "status", "errors", "warnings", "partition_results", "validation_result", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORED_QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    restored_queue_id: str
    start_time: _timestamp_pb2.Timestamp
    completion_time: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    statistics: _restore_statistics_pb2.RestoreStatistics
    status: _restore_status_pb2.RestoreStatus
    errors: _containers.RepeatedCompositeFieldContainer[_restore_error_pb2.RestoreError]
    warnings: _containers.RepeatedCompositeFieldContainer[_restore_warning_pb2.RestoreWarning]
    partition_results: _containers.RepeatedCompositeFieldContainer[_partition_restore_result_pb2.PartitionRestoreResult]
    validation_result: _validation_result_pb2.MetricsValidationResult
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, success: bool = ..., operation_id: _Optional[str] = ..., restored_queue_id: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., statistics: _Optional[_Union[_restore_statistics_pb2.RestoreStatistics, _Mapping]] = ..., status: _Optional[_Union[_restore_status_pb2.RestoreStatus, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[_restore_error_pb2.RestoreError, _Mapping]]] = ..., warnings: _Optional[_Iterable[_Union[_restore_warning_pb2.RestoreWarning, _Mapping]]] = ..., partition_results: _Optional[_Iterable[_Union[_partition_restore_result_pb2.PartitionRestoreResult, _Mapping]]] = ..., validation_result: _Optional[_Union[_validation_result_pb2.MetricsValidationResult, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
