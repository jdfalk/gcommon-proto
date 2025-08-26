from gcommon.v1.common import version_dependency_type_pb2 as _version_dependency_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionDependency(_message.Message):
    __slots__ = ("name", "version", "type", "scope", "constraints", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    type: _version_dependency_type_pb2.VersionDependencyType
    scope: str
    constraints: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., type: _Optional[_Union[_version_dependency_type_pb2.VersionDependencyType, str]] = ..., scope: _Optional[str] = ..., constraints: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
