from gcommon.v1.common import user_details_pb2 as _user_details_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserResponse(_message.Message):
    __slots__ = ("user", "found")
    USER_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    user: _user_details_pb2.UserDetails
    found: bool
    def __init__(self, user: _Optional[_Union[_user_details_pb2.UserDetails, _Mapping]] = ..., found: _Optional[bool] = ...) -> None: ...
