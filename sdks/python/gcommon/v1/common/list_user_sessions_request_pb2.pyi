from gcommon.v1.common import pagination_options_pb2 as _pagination_options_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListUserSessionsRequest(_message.Message):
    __slots__ = ("user_id", "metadata", "pagination", "status_filter", "device_type_filter", "created_after", "created_before", "include_details", "sort_order")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    metadata: _request_metadata_pb2.RequestMetadata
    pagination: _pagination_options_pb2.PaginationOptions
    status_filter: str
    device_type_filter: str
    created_after: _timestamp_pb2.Timestamp
    created_before: _timestamp_pb2.Timestamp
    include_details: bool
    sort_order: str
    def __init__(self, user_id: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., pagination: _Optional[_Union[_pagination_options_pb2.PaginationOptions, _Mapping]] = ..., status_filter: _Optional[str] = ..., device_type_filter: _Optional[str] = ..., created_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., include_details: bool = ..., sort_order: _Optional[str] = ...) -> None: ...
