from gcommon.v1.common import pagination_pb2 as _pagination_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMetricsRequest(_message.Message):
    __slots__ = ("pagination", "name_filter")
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.Pagination
    name_filter: str
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.Pagination, _Mapping]] = ..., name_filter: _Optional[str] = ...) -> None: ...
