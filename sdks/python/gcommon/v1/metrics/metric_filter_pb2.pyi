from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricFilter(_message.Message):
    __slots__ = ("metric_names", "labels", "namespace", "start_timestamp", "end_timestamp", "min_value", "max_value", "include_patterns", "exclude_patterns")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    METRIC_NAMES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    metric_names: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.ScalarMap[str, str]
    namespace: str
    start_timestamp: int
    end_timestamp: int
    min_value: float
    max_value: float
    include_patterns: _containers.RepeatedScalarFieldContainer[str]
    exclude_patterns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, metric_names: _Optional[_Iterable[str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., namespace: _Optional[str] = ..., start_timestamp: _Optional[int] = ..., end_timestamp: _Optional[int] = ..., min_value: _Optional[float] = ..., max_value: _Optional[float] = ..., include_patterns: _Optional[_Iterable[str]] = ..., exclude_patterns: _Optional[_Iterable[str]] = ...) -> None: ...
