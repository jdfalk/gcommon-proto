from gcommon.v1.common import user_preferences_pb2 as _user_preferences_pb2
from gcommon.v1.common import verification_status_pb2 as _verification_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserMetadata(_message.Message):
    __slots__ = ("display_name", "avatar_url", "timezone", "language", "locale", "bio", "website", "location", "birth_date", "gender", "occupation", "company", "custom_fields", "preferences", "verification")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    BIO_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    OCCUPATION_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    avatar_url: str
    timezone: str
    language: str
    locale: str
    bio: str
    website: str
    location: str
    birth_date: _timestamp_pb2.Timestamp
    gender: str
    occupation: str
    company: str
    custom_fields: _containers.ScalarMap[str, str]
    preferences: _user_preferences_pb2.UserPreferences
    verification: _verification_status_pb2.VerificationStatus
    def __init__(self, display_name: _Optional[str] = ..., avatar_url: _Optional[str] = ..., timezone: _Optional[str] = ..., language: _Optional[str] = ..., locale: _Optional[str] = ..., bio: _Optional[str] = ..., website: _Optional[str] = ..., location: _Optional[str] = ..., birth_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., gender: _Optional[str] = ..., occupation: _Optional[str] = ..., company: _Optional[str] = ..., custom_fields: _Optional[_Mapping[str, str]] = ..., preferences: _Optional[_Union[_user_preferences_pb2.UserPreferences, _Mapping]] = ..., verification: _Optional[_Union[_verification_status_pb2.VerificationStatus, _Mapping]] = ...) -> None: ...
