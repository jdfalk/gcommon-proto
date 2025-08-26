from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListUsersRequest(_message.Message):
    __slots__ = ("page", "page_size", "username_filter", "email_filter", "enabled_filter", "role_filter", "sort_by", "sort_direction", "include_deleted")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FILTER_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FILTER_FIELD_NUMBER: _ClassVar[int]
    ROLE_FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    username_filter: str
    email_filter: str
    enabled_filter: bool
    role_filter: str
    sort_by: str
    sort_direction: str
    include_deleted: bool
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ..., username_filter: _Optional[str] = ..., email_filter: _Optional[str] = ..., enabled_filter: bool = ..., role_filter: _Optional[str] = ..., sort_by: _Optional[str] = ..., sort_direction: _Optional[str] = ..., include_deleted: bool = ...) -> None: ...
