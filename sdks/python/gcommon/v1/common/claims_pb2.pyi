from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Claims(_message.Message):
    __slots__ = ("issuer", "subject", "audience", "expires_at", "not_before", "issued_at", "jwt_id", "user_id", "username", "email", "email_verified", "roles", "permissions", "scopes", "mfa_verified", "mfa_method", "session_id", "is_refresh_token", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    NOT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    JWT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    MFA_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    MFA_METHOD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    issuer: str
    subject: str
    audience: _containers.RepeatedScalarFieldContainer[str]
    expires_at: int
    not_before: int
    issued_at: int
    jwt_id: str
    user_id: str
    username: str
    email: str
    email_verified: bool
    roles: _containers.RepeatedScalarFieldContainer[str]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    scopes: _containers.RepeatedScalarFieldContainer[str]
    mfa_verified: bool
    mfa_method: str
    session_id: str
    is_refresh_token: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, issuer: _Optional[str] = ..., subject: _Optional[str] = ..., audience: _Optional[_Iterable[str]] = ..., expires_at: _Optional[int] = ..., not_before: _Optional[int] = ..., issued_at: _Optional[int] = ..., jwt_id: _Optional[str] = ..., user_id: _Optional[str] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., email_verified: _Optional[bool] = ..., roles: _Optional[_Iterable[str]] = ..., permissions: _Optional[_Iterable[str]] = ..., scopes: _Optional[_Iterable[str]] = ..., mfa_verified: _Optional[bool] = ..., mfa_method: _Optional[str] = ..., session_id: _Optional[str] = ..., is_refresh_token: _Optional[bool] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
