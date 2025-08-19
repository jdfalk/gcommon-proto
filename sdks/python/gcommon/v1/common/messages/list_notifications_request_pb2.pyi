from gcommon.v1.common.messages import pagination_pb2 as _pagination_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListNotificationsRequest(_message.Message):
    __slots__ = ("pagination",)
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.Pagination
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.Pagination, _Mapping]] = ...) -> None: ...
