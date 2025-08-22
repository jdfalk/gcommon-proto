from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListApiKeysRequest(_message.Message):
    __slots__ = ("user_id", "include_expired", "page_size", "page_token")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    include_expired: bool
    page_size: int
    page_token: str
    def __init__(self, user_id: _Optional[str] = ..., include_expired: bool = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...
