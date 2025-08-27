import datetime

from gcommon.v1.common import user_status_pb2 as _user_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = (
        "id",
        "username",
        "email",
        "display_name",
        "first_name",
        "last_name",
        "status",
        "created_at",
        "updated_at",
        "last_login_at",
        "email_verified",
        "phone_number",
        "phone_verified",
        "preferences",
        "metadata",
        "avatar_url",
        "timezone",
        "locale",
    )
    class PreferencesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    id: str
    username: str
    email: str
    display_name: str
    first_name: str
    last_name: str
    status: _user_status_pb2.UserStatus
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    last_login_at: _timestamp_pb2.Timestamp
    email_verified: bool
    phone_number: str
    phone_verified: bool
    preferences: _containers.ScalarMap[str, str]
    metadata: _containers.ScalarMap[str, str]
    avatar_url: str
    timezone: str
    locale: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        username: _Optional[str] = ...,
        email: _Optional[str] = ...,
        display_name: _Optional[str] = ...,
        first_name: _Optional[str] = ...,
        last_name: _Optional[str] = ...,
        status: _Optional[_Union[_user_status_pb2.UserStatus, str]] = ...,
        created_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        last_login_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        email_verified: _Optional[bool] = ...,
        phone_number: _Optional[str] = ...,
        phone_verified: _Optional[bool] = ...,
        preferences: _Optional[_Mapping[str, str]] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
        avatar_url: _Optional[str] = ...,
        timezone: _Optional[str] = ...,
        locale: _Optional[str] = ...,
    ) -> None: ...
