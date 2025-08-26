from gcommon.v1.metrics import metric_sample_pb2 as _metric_sample_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeSeries(_message.Message):
    __slots__ = ("metric_id", "samples", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    metric_id: str
    samples: _containers.RepeatedCompositeFieldContainer[_metric_sample_pb2.MetricSample]
    labels: _containers.ScalarMap[str, str]
    def __init__(self, metric_id: _Optional[str] = ..., samples: _Optional[_Iterable[_Union[_metric_sample_pb2.MetricSample, _Mapping]]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...
