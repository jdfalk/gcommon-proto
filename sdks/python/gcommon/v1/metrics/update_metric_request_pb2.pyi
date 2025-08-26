from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import metric_data_pb2 as _metric_data_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateMetricRequest(_message.Message):
    __slots__ = ("metric", "metadata")
    METRIC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metric: _metric_data_pb2.MetricData
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, metric: _Optional[_Union[_metric_data_pb2.MetricData, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
