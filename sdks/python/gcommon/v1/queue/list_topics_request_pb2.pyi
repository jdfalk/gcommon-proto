from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListTopicsRequest(_message.Message):
    __slots__ = ("name_pattern", "namespace", "include_metadata", "include_stats", "limit", "page_token", "sort_by", "sort_order", "topic_states", "access_check", "filters")
    class FiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    TOPIC_STATES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CHECK_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    name_pattern: str
    namespace: str
    include_metadata: bool
    include_stats: bool
    limit: int
    page_token: str
    sort_by: str
    sort_order: str
    topic_states: _containers.RepeatedScalarFieldContainer[str]
    access_check: bool
    filters: _containers.ScalarMap[str, str]
    def __init__(self, name_pattern: _Optional[str] = ..., namespace: _Optional[str] = ..., include_metadata: bool = ..., include_stats: bool = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ..., sort_by: _Optional[str] = ..., sort_order: _Optional[str] = ..., topic_states: _Optional[_Iterable[str]] = ..., access_check: bool = ..., filters: _Optional[_Mapping[str, str]] = ...) -> None: ...
