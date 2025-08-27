from gcommon.v1.common import user_info_pb2 as _user_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserInfoResponse(_message.Message):
    __slots__ = ("user_info", "attributes")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    user_info: _user_info_pb2.UserInfo
    attributes: _containers.ScalarMap[str, str]
    def __init__(
        self,
        user_info: _Optional[_Union[_user_info_pb2.UserInfo, _Mapping]] = ...,
        attributes: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
