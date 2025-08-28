from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import metric_data_pb2 as _metric_data_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordMetricsRequest(_message.Message):
    __slots__ = ("metadata", "metrics", "atomic", "batch_id", "max_retries")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    ATOMIC_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    metrics: _containers.RepeatedCompositeFieldContainer[_metric_data_pb2.MetricData]
    atomic: bool
    batch_id: str
    max_retries: int
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., metrics: _Optional[_Iterable[_Union[_metric_data_pb2.MetricData, _Mapping]]] = ..., atomic: bool = ..., batch_id: _Optional[str] = ..., max_retries: _Optional[int] = ...) -> None: ...
