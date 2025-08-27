from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PeekRequest(_message.Message):
    __slots__ = ("queue_name", "metadata", "max_messages", "start_position", "group_id_filter", "attribute_filters", "message_type_filter", "min_priority", "include_payload", "include_attributes", "include_delivery_metadata")
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
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FILTER_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    MIN_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELIVERY_METADATA_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    metadata: _request_metadata_pb2.RequestMetadata
    max_messages: int
    start_position: int
    group_id_filter: str
    attribute_filters: _containers.ScalarMap[str, str]
    message_type_filter: str
    min_priority: int
    include_payload: bool
    include_attributes: bool
    include_delivery_metadata: bool
    def __init__(self, queue_name: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., max_messages: _Optional[int] = ..., start_position: _Optional[int] = ..., group_id_filter: _Optional[str] = ..., attribute_filters: _Optional[_Mapping[str, str]] = ..., message_type_filter: _Optional[str] = ..., min_priority: _Optional[int] = ..., include_payload: _Optional[bool] = ..., include_attributes: _Optional[bool] = ..., include_delivery_metadata: _Optional[bool] = ...) -> None: ...
