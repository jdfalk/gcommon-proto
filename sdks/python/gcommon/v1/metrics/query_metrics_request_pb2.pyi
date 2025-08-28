from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import metric_query_pb2 as _metric_query_pb2
from gcommon.v1.metrics import query_output_options_pb2 as _query_output_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryMetricsRequest(_message.Message):
    __slots__ = ("metadata", "query", "timeout_seconds", "include_query_plan", "metadata_only", "output_options")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_QUERY_PLAN_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    query: _metric_query_pb2.MetricQuery
    timeout_seconds: int
    include_query_plan: bool
    metadata_only: bool
    output_options: _query_output_options_pb2.QueryOutputOptions
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., query: _Optional[_Union[_metric_query_pb2.MetricQuery, _Mapping]] = ..., timeout_seconds: _Optional[int] = ..., include_query_plan: bool = ..., metadata_only: bool = ..., output_options: _Optional[_Union[_query_output_options_pb2.QueryOutputOptions, _Mapping]] = ...) -> None: ...
