from gcommon.v1.common import dependency_type_pb2 as _dependency_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValueDependency(_message.Message):
    __slots__ = ("type", "dependent_key", "dependency_key", "condition", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENT_KEY_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    type: _dependency_type_pb2.DependencyType
    dependent_key: str
    dependency_key: str
    condition: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[_Union[_dependency_type_pb2.DependencyType, str]] = ..., dependent_key: _Optional[str] = ..., dependency_key: _Optional[str] = ..., condition: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
