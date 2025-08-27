import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUserResponse(_message.Message):
    __slots__ = (
        "user_id",
        "username",
        "email",
        "full_name",
        "enabled",
        "roles",
        "created_at",
        "email_verification_required",
        "verification_token",
        "expires_at",
    )
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFICATION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    username: str
    email: str
    full_name: str
    enabled: bool
    roles: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    email_verification_required: bool
    verification_token: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        user_id: _Optional[str] = ...,
        username: _Optional[str] = ...,
        email: _Optional[str] = ...,
        full_name: _Optional[str] = ...,
        enabled: _Optional[bool] = ...,
        roles: _Optional[_Iterable[str]] = ...,
        created_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        email_verification_required: _Optional[bool] = ...,
        verification_token: _Optional[str] = ...,
        expires_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
