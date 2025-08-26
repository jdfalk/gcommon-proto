from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import metric_data_pb2 as _metric_data_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportMetricsRequest(_message.Message):
    __slots__ = ("metrics", "metadata")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[_metric_data_pb2.MetricData]
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, metrics: _Optional[_Iterable[_Union[_metric_data_pb2.MetricData, _Mapping]]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
