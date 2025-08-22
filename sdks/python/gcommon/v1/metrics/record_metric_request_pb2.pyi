from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import batch_context_pb2 as _batch_context_pb2
from gcommon.v1.metrics import metric_data_pb2 as _metric_data_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordMetricRequest(_message.Message):
    __slots__ = ("metadata", "metric", "provider_id", "validate", "timestamp", "batch_context")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BATCH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    metric: _metric_data_pb2.MetricData
    provider_id: str
    validate: bool
    timestamp: _timestamp_pb2.Timestamp
    batch_context: _batch_context_pb2.BatchContext
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., metric: _Optional[_Union[_metric_data_pb2.MetricData, _Mapping]] = ..., provider_id: _Optional[str] = ..., validate: bool = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., batch_context: _Optional[_Union[_batch_context_pb2.BatchContext, _Mapping]] = ...) -> None: ...
