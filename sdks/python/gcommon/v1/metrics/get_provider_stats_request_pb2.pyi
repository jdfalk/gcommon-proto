from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.common import time_range_metrics_pb2 as _time_range_metrics_pb2
from gcommon.v1.metrics import stats_options_pb2 as _stats_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProviderStatsRequest(_message.Message):
    __slots__ = ("metadata", "provider_id", "time_range", "options", "granularity", "include_realtime")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REALTIME_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    provider_id: str
    time_range: _time_range_metrics_pb2.TimeRangeMetrics
    options: _stats_options_pb2.StatsOptions
    granularity: str
    include_realtime: bool
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., provider_id: _Optional[str] = ..., time_range: _Optional[_Union[_time_range_metrics_pb2.TimeRangeMetrics, _Mapping]] = ..., options: _Optional[_Union[_stats_options_pb2.StatsOptions, _Mapping]] = ..., granularity: _Optional[str] = ..., include_realtime: bool = ...) -> None: ...
