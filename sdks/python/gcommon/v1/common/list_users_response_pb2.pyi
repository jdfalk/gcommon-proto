from gcommon.v1.common import user_info_pb2 as _user_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "total_count", "page", "page_size", "total_pages", "has_next_page", "has_previous_page")
    USERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    HAS_NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    HAS_PREVIOUS_PAGE_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_info_pb2.UserInfo]
    total_count: int
    page: int
    page_size: int
    total_pages: int
    has_next_page: bool
    has_previous_page: bool
    def __init__(self, users: _Optional[_Iterable[_Union[_user_info_pb2.UserInfo, _Mapping]]] = ..., total_count: _Optional[int] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., total_pages: _Optional[int] = ..., has_next_page: _Optional[bool] = ..., has_previous_page: _Optional[bool] = ...) -> None: ...
