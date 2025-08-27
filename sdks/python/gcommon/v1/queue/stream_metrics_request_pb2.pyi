from gcommon.v1.common import metric_type_pb2 as _metric_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueStreamMetricsRequest(_message.Message):
    __slots__ = ("queue_names", "metric_types", "interval_seconds")
    QUEUE_NAMES_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPES_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    queue_names: _containers.RepeatedScalarFieldContainer[str]
    metric_types: _containers.RepeatedScalarFieldContainer[
        _metric_type_pb2.MetricsMetricType
    ]
    interval_seconds: int
    def __init__(
        self,
        queue_names: _Optional[_Iterable[str]] = ...,
        metric_types: _Optional[
            _Iterable[_Union[_metric_type_pb2.MetricsMetricType, str]]
        ] = ...,
        interval_seconds: _Optional[int] = ...,
    ) -> None: ...
