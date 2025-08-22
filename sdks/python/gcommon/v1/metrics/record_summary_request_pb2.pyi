from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import summary_metric_pb2 as _summary_metric_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordSummaryRequest(_message.Message):
    __slots__ = ("metric", "observed_at", "metadata")
    METRIC_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metric: _summary_metric_pb2.SummaryMetric
    observed_at: _timestamp_pb2.Timestamp
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, metric: _Optional[_Union[_summary_metric_pb2.SummaryMetric, _Mapping]] = ..., observed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
