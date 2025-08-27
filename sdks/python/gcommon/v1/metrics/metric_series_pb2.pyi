from gcommon.v1.common import metric_type_pb2 as _metric_type_pb2
from gcommon.v1.metrics import metric_value_pb2 as _metric_value_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricSeries(_message.Message):
    __slots__ = ("name", "type", "labels", "values", "step_seconds")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    STEP_SECONDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _metric_type_pb2.MetricsMetricType
    labels: _containers.ScalarMap[str, str]
    values: _containers.RepeatedCompositeFieldContainer[_metric_value_pb2.MetricValue]
    step_seconds: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_metric_type_pb2.MetricsMetricType, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., values: _Optional[_Iterable[_Union[_metric_value_pb2.MetricValue, _Mapping]]] = ..., step_seconds: _Optional[int] = ...) -> None: ...
