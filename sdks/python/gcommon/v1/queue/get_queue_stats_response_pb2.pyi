from gcommon.v1.common import metrics_error_stats_pb2 as _metrics_error_stats_pb2
from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from gcommon.v1.queue import consumer_stats_pb2 as _consumer_stats_pb2
from gcommon.v1.queue import historical_stats_pb2 as _historical_stats_pb2
from gcommon.v1.queue import performance_metrics_pb2 as _performance_metrics_pb2
from gcommon.v1.queue import queue_stats_pb2 as _queue_stats_pb2
from gcommon.v1.queue import queue_stats_summary_pb2 as _queue_stats_summary_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetQueueStatsResponse(_message.Message):
    __slots__ = ("metadata", "summary", "queue_stats", "consumer_stats", "historical_stats", "error_stats", "performance_metrics", "generated_at")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    QUEUE_STATS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_STATS_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_STATS_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    metadata: _response_metadata_pb2.ResponseMetadata
    summary: _queue_stats_summary_pb2.QueueStatsSummary
    queue_stats: _containers.RepeatedCompositeFieldContainer[_queue_stats_pb2.QueueStats]
    consumer_stats: _containers.RepeatedCompositeFieldContainer[_consumer_stats_pb2.ConsumerStats]
    historical_stats: _historical_stats_pb2.HistoricalStats
    error_stats: _metrics_error_stats_pb2.MetricsErrorStats
    performance_metrics: _performance_metrics_pb2.PerformanceMetrics
    generated_at: _timestamp_pb2.Timestamp
    def __init__(self, metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ..., summary: _Optional[_Union[_queue_stats_summary_pb2.QueueStatsSummary, _Mapping]] = ..., queue_stats: _Optional[_Iterable[_Union[_queue_stats_pb2.QueueStats, _Mapping]]] = ..., consumer_stats: _Optional[_Iterable[_Union[_consumer_stats_pb2.ConsumerStats, _Mapping]]] = ..., historical_stats: _Optional[_Union[_historical_stats_pb2.HistoricalStats, _Mapping]] = ..., error_stats: _Optional[_Union[_metrics_error_stats_pb2.MetricsErrorStats, _Mapping]] = ..., performance_metrics: _Optional[_Union[_performance_metrics_pb2.PerformanceMetrics, _Mapping]] = ..., generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
