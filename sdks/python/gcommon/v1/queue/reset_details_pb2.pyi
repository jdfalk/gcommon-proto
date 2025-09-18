from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResetDetails(_message.Message):
    __slots__ = ("metrics_reset_count", "counters_reset_count", "histograms_reset_count", "partitions_affected", "reset_duration_ms", "partial_reset", "reset_reason", "initiated_by")
    METRICS_RESET_COUNT_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_RESET_COUNT_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAMS_RESET_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_AFFECTED_FIELD_NUMBER: _ClassVar[int]
    RESET_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_RESET_FIELD_NUMBER: _ClassVar[int]
    RESET_REASON_FIELD_NUMBER: _ClassVar[int]
    INITIATED_BY_FIELD_NUMBER: _ClassVar[int]
    metrics_reset_count: int
    counters_reset_count: int
    histograms_reset_count: int
    partitions_affected: int
    reset_duration_ms: int
    partial_reset: bool
    reset_reason: str
    initiated_by: str
    def __init__(self, metrics_reset_count: _Optional[int] = ..., counters_reset_count: _Optional[int] = ..., histograms_reset_count: _Optional[int] = ..., partitions_affected: _Optional[int] = ..., reset_duration_ms: _Optional[int] = ..., partial_reset: _Optional[bool] = ..., reset_reason: _Optional[str] = ..., initiated_by: _Optional[str] = ...) -> None: ...
