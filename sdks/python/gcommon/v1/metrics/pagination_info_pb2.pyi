from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsPaginationInfo(_message.Message):
    __slots__ = ("page", "page_size", "total_items", "total_pages", "has_next", "has_previous", "next_cursor", "previous_cursor")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    HAS_NEXT_FIELD_NUMBER: _ClassVar[int]
    HAS_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_CURSOR_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    total_items: int
    total_pages: int
    has_next: bool
    has_previous: bool
    next_cursor: str
    previous_cursor: str
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ..., total_items: _Optional[int] = ..., total_pages: _Optional[int] = ..., has_next: _Optional[bool] = ..., has_previous: _Optional[bool] = ..., next_cursor: _Optional[str] = ..., previous_cursor: _Optional[str] = ...) -> None: ...
