from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics.messages import buffer_config_pb2 as _buffer_config_pb2
from gcommon.v1.metrics.messages import metric_filter_pb2 as _metric_filter_pb2
from gcommon.v1.metrics.messages import stream_options_pb2 as _stream_options_pb2
from gcommon.v1.metrics.messages import stream_start_pb2 as _stream_start_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsStreamMetricsRequest(_message.Message):
    __slots__ = ("metadata", "filter", "options", "provider_id", "start", "buffer_config")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    BUFFER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    filter: _metric_filter_pb2.MetricFilter
    options: _stream_options_pb2.StreamOptions
    provider_id: str
    start: _stream_start_pb2.StreamStart
    buffer_config: _buffer_config_pb2.BufferConfig
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., filter: _Optional[_Union[_metric_filter_pb2.MetricFilter, _Mapping]] = ..., options: _Optional[_Union[_stream_options_pb2.StreamOptions, _Mapping]] = ..., provider_id: _Optional[str] = ..., start: _Optional[_Union[_stream_start_pb2.StreamStart, _Mapping]] = ..., buffer_config: _Optional[_Union[_buffer_config_pb2.BufferConfig, _Mapping]] = ...) -> None: ...
