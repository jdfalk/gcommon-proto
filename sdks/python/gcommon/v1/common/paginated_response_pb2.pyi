from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaginatedResponse(_message.Message):
    __slots__ = ("next_page_token", "prev_page_token", "total_count", "current_page", "total_pages", "page_size")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    prev_page_token: str
    total_count: int
    current_page: int
    total_pages: int
    page_size: int
    def __init__(self, next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ..., total_count: _Optional[int] = ..., current_page: _Optional[int] = ..., total_pages: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...
