from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HierarchyNode(_message.Message):
    __slots__ = ("id", "name", "node_type", "entity_id", "parent_id", "child_ids", "level", "position", "path", "manager_id", "metadata", "active")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_IDS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MANAGER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    node_type: str
    entity_id: str
    parent_id: str
    child_ids: _containers.RepeatedScalarFieldContainer[str]
    level: int
    position: int
    path: str
    manager_id: str
    metadata: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    active: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., node_type: _Optional[str] = ..., entity_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., child_ids: _Optional[_Iterable[str]] = ..., level: _Optional[int] = ..., position: _Optional[int] = ..., path: _Optional[str] = ..., manager_id: _Optional[str] = ..., metadata: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ..., active: bool = ...) -> None: ...
