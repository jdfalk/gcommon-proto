from gcommon.v1.queue import api_key_auth_pb2 as _api_key_auth_pb2
from gcommon.v1.queue import external_auth_service_pb2 as _external_auth_service_pb2
from gcommon.v1.queue import jwt_auth_pb2 as _jwt_auth_pb2
from gcommon.v1.queue import permission_rule_pb2 as _permission_rule_pb2
from gcommon.v1.queue import role_based_access_control_pb2 as _role_based_access_control_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizationConfig(_message.Message):
    __slots__ = ("enabled", "default_policy", "rules", "rbac", "api_key_auth", "jwt_auth", "external_auth")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_POLICY_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    RBAC_FIELD_NUMBER: _ClassVar[int]
    API_KEY_AUTH_FIELD_NUMBER: _ClassVar[int]
    JWT_AUTH_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_AUTH_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    default_policy: str
    rules: _containers.RepeatedCompositeFieldContainer[_permission_rule_pb2.PermissionRule]
    rbac: _role_based_access_control_pb2.RoleBasedAccessControl
    api_key_auth: _api_key_auth_pb2.APIKeyAuth
    jwt_auth: _jwt_auth_pb2.JwtAuth
    external_auth: _external_auth_service_pb2.ExternalAuthService
    def __init__(self, enabled: _Optional[bool] = ..., default_policy: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[_permission_rule_pb2.PermissionRule, _Mapping]]] = ..., rbac: _Optional[_Union[_role_based_access_control_pb2.RoleBasedAccessControl, _Mapping]] = ..., api_key_auth: _Optional[_Union[_api_key_auth_pb2.APIKeyAuth, _Mapping]] = ..., jwt_auth: _Optional[_Union[_jwt_auth_pb2.JwtAuth, _Mapping]] = ..., external_auth: _Optional[_Union[_external_auth_service_pb2.ExternalAuthService, _Mapping]] = ...) -> None: ...
