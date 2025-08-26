from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HierarchyPath(_message.Message):
    __slots__ = ("descendant_id", "ancestor_id", "distance", "path_nodes")
    DESCENDANT_ID_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    PATH_NODES_FIELD_NUMBER: _ClassVar[int]
    descendant_id: str
    ancestor_id: str
    distance: int
    path_nodes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, descendant_id: _Optional[str] = ..., ancestor_id: _Optional[str] = ..., distance: _Optional[int] = ..., path_nodes: _Optional[_Iterable[str]] = ...) -> None: ...
