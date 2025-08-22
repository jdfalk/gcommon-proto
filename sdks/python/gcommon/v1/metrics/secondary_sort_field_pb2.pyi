from gcommon.v1.common import sort_direction_pb2 as _sort_direction_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecondarySortField(_message.Message):
    __slots__ = ("field", "direction")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    field: str
    direction: _sort_direction_pb2.SortDirection
    def __init__(self, field: _Optional[str] = ..., direction: _Optional[_Union[_sort_direction_pb2.SortDirection, str]] = ...) -> None: ...
