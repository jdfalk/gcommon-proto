from gcommon.v1.common import permission_condition_pb2 as _permission_condition_pb2
from gcommon.v1.common import permission_level_pb2 as _permission_level_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionMetadata(_message.Message):
    __slots__ = ("permission_id", "name", "resource_types", "actions", "conditions", "level", "created_at", "created_by")
    PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    permission_id: str
    name: str
    resource_types: _containers.RepeatedScalarFieldContainer[str]
    actions: _containers.RepeatedScalarFieldContainer[str]
    conditions: _containers.RepeatedCompositeFieldContainer[_permission_condition_pb2.PermissionCondition]
    level: _permission_level_pb2.AuthPermissionLevel
    created_at: int
    created_by: str
    def __init__(self, permission_id: _Optional[str] = ..., name: _Optional[str] = ..., resource_types: _Optional[_Iterable[str]] = ..., actions: _Optional[_Iterable[str]] = ..., conditions: _Optional[_Iterable[_Union[_permission_condition_pb2.PermissionCondition, _Mapping]]] = ..., level: _Optional[_Union[_permission_level_pb2.AuthPermissionLevel, str]] = ..., created_at: _Optional[int] = ..., created_by: _Optional[str] = ...) -> None: ...
