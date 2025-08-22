from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterUserRequest(_message.Message):
    __slots__ = ("username", "email", "password", "first_name", "last_name", "phone_number", "organization_id", "require_email_verification", "invitation_token", "metadata", "request_metadata", "tos_accepted_at", "privacy_accepted_at")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_EMAIL_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    INVITATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    TOS_ACCEPTED_AT_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_ACCEPTED_AT_FIELD_NUMBER: _ClassVar[int]
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    phone_number: str
    organization_id: str
    require_email_verification: bool
    invitation_token: str
    metadata: _containers.ScalarMap[str, str]
    request_metadata: _request_metadata_pb2.RequestMetadata
    tos_accepted_at: int
    privacy_accepted_at: int
    def __init__(self, username: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., phone_number: _Optional[str] = ..., organization_id: _Optional[str] = ..., require_email_verification: bool = ..., invitation_token: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., request_metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., tos_accepted_at: _Optional[int] = ..., privacy_accepted_at: _Optional[int] = ...) -> None: ...
