from gcommon.v1.common.enums import role_scope_pb2 as _role_scope_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoleAssignment(_message.Message):
    __slots__ = ("id", "user_id", "role_id", "resource", "scope", "created_at", "expires_at", "assigned_by_user_id", "metadata", "active")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    role_id: str
    resource: str
    scope: _role_scope_pb2.RoleScope
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    assigned_by_user_id: str
    metadata: _containers.ScalarMap[str, str]
    active: bool
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., role_id: _Optional[str] = ..., resource: _Optional[str] = ..., scope: _Optional[_Union[_role_scope_pb2.RoleScope, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assigned_by_user_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., active: bool = ...) -> None: ...
