from gcommon.v1.common import filter_value_pb2 as _filter_value_pb2
from gcommon.v1.common import metrics_time_range_pb2 as _metrics_time_range_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FilterOptions(_message.Message):
    __slots__ = ("filters", "search_query", "time_range")
    class FiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _filter_value_pb2.FilterValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_filter_value_pb2.FilterValue, _Mapping]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.MessageMap[str, _filter_value_pb2.FilterValue]
    search_query: str
    time_range: _metrics_time_range_pb2.CommonTimeRange
    def __init__(self, filters: _Optional[_Mapping[str, _filter_value_pb2.FilterValue]] = ..., search_query: _Optional[str] = ..., time_range: _Optional[_Union[_metrics_time_range_pb2.CommonTimeRange, _Mapping]] = ...) -> None: ...
