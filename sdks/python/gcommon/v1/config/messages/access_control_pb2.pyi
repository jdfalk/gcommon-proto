from gcommon.v1.config.messages import access_restriction_pb2 as _access_restriction_pb2
from gcommon.v1.config.messages import rate_limits_pb2 as _rate_limits_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigAccessControl(_message.Message):
    __slots__ = ("policy", "allowed_users", "allowed_roles", "allowed_services", "allowed_environments", "restrictions", "max_access_count", "rate_limits", "approval_required", "audit_enabled")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_USERS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ROLES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_ACCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    AUDIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    policy: str
    allowed_users: _containers.RepeatedScalarFieldContainer[str]
    allowed_roles: _containers.RepeatedScalarFieldContainer[str]
    allowed_services: _containers.RepeatedScalarFieldContainer[str]
    allowed_environments: _containers.RepeatedScalarFieldContainer[str]
    restrictions: _containers.RepeatedCompositeFieldContainer[_access_restriction_pb2.AccessRestriction]
    max_access_count: int
    rate_limits: _rate_limits_pb2.RateLimits
    approval_required: bool
    audit_enabled: bool
    def __init__(self, policy: _Optional[str] = ..., allowed_users: _Optional[_Iterable[str]] = ..., allowed_roles: _Optional[_Iterable[str]] = ..., allowed_services: _Optional[_Iterable[str]] = ..., allowed_environments: _Optional[_Iterable[str]] = ..., restrictions: _Optional[_Iterable[_Union[_access_restriction_pb2.AccessRestriction, _Mapping]]] = ..., max_access_count: _Optional[int] = ..., rate_limits: _Optional[_Union[_rate_limits_pb2.RateLimits, _Mapping]] = ..., approval_required: bool = ..., audit_enabled: bool = ...) -> None: ...
