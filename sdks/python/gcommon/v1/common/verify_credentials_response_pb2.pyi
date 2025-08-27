from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import user_info_pb2 as _user_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyCredentialsResponse(_message.Message):
    __slots__ = ("verified", "user_info", "error")
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    verified: bool
    user_info: _user_info_pb2.UserInfo
    error: _error_pb2.Error
    def __init__(
        self,
        verified: _Optional[bool] = ...,
        user_info: _Optional[_Union[_user_info_pb2.UserInfo, _Mapping]] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
    ) -> None: ...
