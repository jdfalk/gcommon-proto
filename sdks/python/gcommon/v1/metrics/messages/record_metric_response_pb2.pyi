from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.metrics.messages import recording_stats_pb2 as _recording_stats_pb2
from gcommon.v1.metrics.messages import validation_result_pb2 as _validation_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordMetricResponse(_message.Message):
    __slots__ = ("success", "error", "metric_id", "recorded_at", "provider_id", "validation", "stats", "warnings")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    metric_id: str
    recorded_at: _timestamp_pb2.Timestamp
    provider_id: str
    validation: _validation_result_pb2.MetricsValidationResult
    stats: _recording_stats_pb2.RecordingStats
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., metric_id: _Optional[str] = ..., recorded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., provider_id: _Optional[str] = ..., validation: _Optional[_Union[_validation_result_pb2.MetricsValidationResult, _Mapping]] = ..., stats: _Optional[_Union[_recording_stats_pb2.RecordingStats, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...
