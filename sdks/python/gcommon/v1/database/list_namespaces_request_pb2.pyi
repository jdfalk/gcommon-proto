from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListNamespacesRequest(_message.Message):
    __slots__ = ("page", "page_size", "name_filter", "include_stats")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATS_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    name_filter: str
    include_stats: bool
    def __init__(
        self,
        page: _Optional[int] = ...,
        page_size: _Optional[int] = ...,
        name_filter: _Optional[str] = ...,
        include_stats: _Optional[bool] = ...,
    ) -> None: ...
