from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserRequest(_message.Message):
    __slots__ = ("user_id", "include_details", "include_deleted", "fields")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    include_details: bool
    include_deleted: bool
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        user_id: _Optional[str] = ...,
        include_details: _Optional[bool] = ...,
        include_deleted: _Optional[bool] = ...,
        fields: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
