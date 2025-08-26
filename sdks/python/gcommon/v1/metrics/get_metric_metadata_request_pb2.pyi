from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetMetricMetadataRequest(_message.Message):
    __slots__ = ("provider_id", "metric_names", "namespace", "include_inactive", "page_size", "page_token", "metric_type", "label_filters", "include_retention_info", "include_usage_stats")
    class LabelFiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAMES_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FILTERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RETENTION_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_USAGE_STATS_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    metric_names: _containers.RepeatedScalarFieldContainer[str]
    namespace: str
    include_inactive: bool
    page_size: int
    page_token: str
    metric_type: str
    label_filters: _containers.ScalarMap[str, str]
    include_retention_info: bool
    include_usage_stats: bool
    def __init__(self, provider_id: _Optional[str] = ..., metric_names: _Optional[_Iterable[str]] = ..., namespace: _Optional[str] = ..., include_inactive: _Optional[bool] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., metric_type: _Optional[str] = ..., label_filters: _Optional[_Mapping[str, str]] = ..., include_retention_info: _Optional[bool] = ..., include_usage_stats: _Optional[bool] = ...) -> None: ...
