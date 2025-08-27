from gcommon.v1.common import pagination_pb2 as _pagination_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthListSessionsRequest(_message.Message):
    __slots__ = ("pagination", "user_id", "status")
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.Pagination
    user_id: str
    status: str
    def __init__(
        self,
        pagination: _Optional[_Union[_pagination_pb2.Pagination, _Mapping]] = ...,
        user_id: _Optional[str] = ...,
        status: _Optional[str] = ...,
    ) -> None: ...
