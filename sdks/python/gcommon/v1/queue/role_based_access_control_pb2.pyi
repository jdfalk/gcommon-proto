from gcommon.v1.queue import external_role_provider_pb2 as _external_role_provider_pb2
from gcommon.v1.queue import role_inheritance_pb2 as _role_inheritance_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoleBasedAccessControl(_message.Message):
    __slots__ = ("enabled", "default_roles", "role_inheritance", "external_provider")
    class RoleInheritanceEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _role_inheritance_pb2.RoleInheritance
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_role_inheritance_pb2.RoleInheritance, _Mapping]] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROLES_FIELD_NUMBER: _ClassVar[int]
    ROLE_INHERITANCE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    default_roles: _containers.RepeatedScalarFieldContainer[str]
    role_inheritance: _containers.MessageMap[str, _role_inheritance_pb2.RoleInheritance]
    external_provider: _external_role_provider_pb2.ExternalRoleProvider
    def __init__(self, enabled: bool = ..., default_roles: _Optional[_Iterable[str]] = ..., role_inheritance: _Optional[_Mapping[str, _role_inheritance_pb2.RoleInheritance]] = ..., external_provider: _Optional[_Union[_external_role_provider_pb2.ExternalRoleProvider, _Mapping]] = ...) -> None: ...
