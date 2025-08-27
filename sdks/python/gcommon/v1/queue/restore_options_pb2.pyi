from gcommon.v1.common import time_range_metrics_pb2 as _time_range_metrics_pb2
from gcommon.v1.queue import filter_criteria_pb2 as _filter_criteria_pb2
from gcommon.v1.queue import offset_range_pb2 as _offset_range_pb2
from gcommon.v1.queue import performance_options_pb2 as _performance_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreOptions(_message.Message):
    __slots__ = (
        "skip_message_content",
        "metadata_only",
        "max_messages",
        "offset_range",
        "time_range",
        "priority_levels",
        "filter_criteria",
        "performance",
    )
    SKIP_MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    OFFSET_RANGE_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_LEVELS_FIELD_NUMBER: _ClassVar[int]
    FILTER_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    skip_message_content: bool
    metadata_only: bool
    max_messages: int
    offset_range: _offset_range_pb2.OffsetRange
    time_range: _time_range_metrics_pb2.TimeRangeMetrics
    priority_levels: _containers.RepeatedScalarFieldContainer[int]
    filter_criteria: _filter_criteria_pb2.FilterCriteria
    performance: _performance_options_pb2.PerformanceOptions
    def __init__(
        self,
        skip_message_content: _Optional[bool] = ...,
        metadata_only: _Optional[bool] = ...,
        max_messages: _Optional[int] = ...,
        offset_range: _Optional[_Union[_offset_range_pb2.OffsetRange, _Mapping]] = ...,
        time_range: _Optional[
            _Union[_time_range_metrics_pb2.TimeRangeMetrics, _Mapping]
        ] = ...,
        priority_levels: _Optional[_Iterable[int]] = ...,
        filter_criteria: _Optional[
            _Union[_filter_criteria_pb2.FilterCriteria, _Mapping]
        ] = ...,
        performance: _Optional[
            _Union[_performance_options_pb2.PerformanceOptions, _Mapping]
        ] = ...,
    ) -> None: ...
