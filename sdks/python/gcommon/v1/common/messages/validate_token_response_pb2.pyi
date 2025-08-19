from gcommon.v1.common.messages import user_info_pb2 as _user_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateTokenResponse(_message.Message):
    __slots__ = ("valid", "expires_at", "user_info", "scopes", "subject", "issuer", "expires_in")
    VALID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    expires_at: _timestamp_pb2.Timestamp
    user_info: _user_info_pb2.UserInfo
    scopes: _containers.RepeatedScalarFieldContainer[str]
    subject: str
    issuer: str
    expires_in: int
    def __init__(self, valid: bool = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_info: _Optional[_Union[_user_info_pb2.UserInfo, _Mapping]] = ..., scopes: _Optional[_Iterable[str]] = ..., subject: _Optional[str] = ..., issuer: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...
