from gcommon.v1.common import health_metric_data_pb2 as _health_metric_data_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHealthMetricsResponse(_message.Message):
    __slots__ = ("metrics", "metadata")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[_health_metric_data_pb2.HealthMetricData]
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, metrics: _Optional[_Iterable[_Union[_health_metric_data_pb2.HealthMetricData, _Mapping]]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
