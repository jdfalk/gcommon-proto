from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommonPaginationInfo(_message.Message):
    __slots__ = (
        "current_page",
        "page_size",
        "total_items",
        "total_pages",
        "has_next",
        "has_previous",
        "next_page_token",
        "previous_page_token",
    )
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    HAS_NEXT_FIELD_NUMBER: _ClassVar[int]
    HAS_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    page_size: int
    total_items: int
    total_pages: int
    has_next: bool
    has_previous: bool
    next_page_token: str
    previous_page_token: str
    def __init__(
        self,
        current_page: _Optional[int] = ...,
        page_size: _Optional[int] = ...,
        total_items: _Optional[int] = ...,
        total_pages: _Optional[int] = ...,
        has_next: _Optional[bool] = ...,
        has_previous: _Optional[bool] = ...,
        next_page_token: _Optional[str] = ...,
        previous_page_token: _Optional[str] = ...,
    ) -> None: ...
