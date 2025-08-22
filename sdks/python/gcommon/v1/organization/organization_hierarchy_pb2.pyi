from gcommon.v1.common import hierarchy_type_pb2 as _hierarchy_type_pb2
from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from gcommon.v1.organization import hierarchy_node_pb2 as _hierarchy_node_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationHierarchy(_message.Message):
    __slots__ = ("id", "organization_id", "hierarchy_type", "name", "description", "root_node", "active", "metadata", "created_at", "updated_at", "created_by", "updated_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    hierarchy_type: _hierarchy_type_pb2.HierarchyType
    name: str
    description: str
    root_node: _hierarchy_node_pb2.HierarchyNode
    active: bool
    metadata: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: str
    updated_by: str
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., hierarchy_type: _Optional[_Union[_hierarchy_type_pb2.HierarchyType, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., root_node: _Optional[_Union[_hierarchy_node_pb2.HierarchyNode, _Mapping]] = ..., active: bool = ..., metadata: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., updated_by: _Optional[str] = ...) -> None: ...
