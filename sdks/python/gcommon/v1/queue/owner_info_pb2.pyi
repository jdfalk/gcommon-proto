import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OwnerInfo(_message.Message):
    __slots__ = ("user_id", "username", "email", "organization", "owned_since")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    OWNED_SINCE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    username: str
    email: str
    organization: str
    owned_since: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., organization: _Optional[str] = ..., owned_since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
