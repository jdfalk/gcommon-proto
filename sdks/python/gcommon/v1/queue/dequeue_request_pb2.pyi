from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DequeueRequest(_message.Message):
    __slots__ = ("queue_name", "metadata", "max_messages", "visibility_timeout", "wait_time", "group_id_filter", "attribute_filters", "message_type_filter", "consumer_id", "include_attributes", "include_metadata", "peek_only", "min_priority")
    class AttributeFiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FILTER_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    PEEK_ONLY_FIELD_NUMBER: _ClassVar[int]
    MIN_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    metadata: _request_metadata_pb2.RequestMetadata
    max_messages: int
    visibility_timeout: _duration_pb2.Duration
    wait_time: _duration_pb2.Duration
    group_id_filter: str
    attribute_filters: _containers.ScalarMap[str, str]
    message_type_filter: str
    consumer_id: str
    include_attributes: bool
    include_metadata: bool
    peek_only: bool
    min_priority: int
    def __init__(self, queue_name: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., max_messages: _Optional[int] = ..., visibility_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., wait_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., group_id_filter: _Optional[str] = ..., attribute_filters: _Optional[_Mapping[str, str]] = ..., message_type_filter: _Optional[str] = ..., consumer_id: _Optional[str] = ..., include_attributes: bool = ..., include_metadata: bool = ..., peek_only: bool = ..., min_priority: _Optional[int] = ...) -> None: ...
