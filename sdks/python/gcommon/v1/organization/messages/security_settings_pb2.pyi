from gcommon.v1.organization.messages import rate_limit_config_pb2 as _rate_limit_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecuritySettings(_message.Message):
    __slots__ = ("require_mfa", "min_password_length", "require_password_complexity", "password_expiry_days", "session_timeout_minutes", "sso_enabled", "sso_providers", "ip_whitelist", "api_access_enabled", "api_rate_limit", "audit_log_retention_days")
    REQUIRE_MFA_FIELD_NUMBER: _ClassVar[int]
    MIN_PASSWORD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PASSWORD_COMPLEXITY_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_EXPIRY_DAYS_FIELD_NUMBER: _ClassVar[int]
    SESSION_TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    SSO_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SSO_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    IP_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    API_RATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    AUDIT_LOG_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    require_mfa: bool
    min_password_length: int
    require_password_complexity: bool
    password_expiry_days: int
    session_timeout_minutes: int
    sso_enabled: bool
    sso_providers: _containers.RepeatedScalarFieldContainer[str]
    ip_whitelist: _containers.RepeatedScalarFieldContainer[str]
    api_access_enabled: bool
    api_rate_limit: _rate_limit_config_pb2.OrganizationRateLimitConfig
    audit_log_retention_days: int
    def __init__(self, require_mfa: bool = ..., min_password_length: _Optional[int] = ..., require_password_complexity: bool = ..., password_expiry_days: _Optional[int] = ..., session_timeout_minutes: _Optional[int] = ..., sso_enabled: bool = ..., sso_providers: _Optional[_Iterable[str]] = ..., ip_whitelist: _Optional[_Iterable[str]] = ..., api_access_enabled: bool = ..., api_rate_limit: _Optional[_Union[_rate_limit_config_pb2.OrganizationRateLimitConfig, _Mapping]] = ..., audit_log_retention_days: _Optional[int] = ...) -> None: ...
