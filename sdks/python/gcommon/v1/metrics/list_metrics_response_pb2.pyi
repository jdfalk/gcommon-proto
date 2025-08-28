from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import metric_metadata_pb2 as _metric_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMetricsResponse(_message.Message):
    __slots__ = ("metrics", "error")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[_metric_metadata_pb2.MetricMetadata]
    error: _error_pb2.Error
    def __init__(self, metrics: _Optional[_Iterable[_Union[_metric_metadata_pb2.MetricMetadata, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
