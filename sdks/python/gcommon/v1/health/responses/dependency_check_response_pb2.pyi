from gcommon.v1.health.messages import dependency_check_pb2 as _dependency_check_pb2
from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DependencyCheckResponse(_message.Message):
    __slots__ = ("dependencies", "all_dependencies_healthy", "healthy_count", "unhealthy_count", "metadata", "issues")
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    ALL_DEPENDENCIES_HEALTHY_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_COUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    dependencies: _containers.RepeatedCompositeFieldContainer[_dependency_check_pb2.DependencyCheck]
    all_dependencies_healthy: bool
    healthy_count: int
    unhealthy_count: int
    metadata: _response_metadata_pb2.ResponseMetadata
    issues: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dependencies: _Optional[_Iterable[_Union[_dependency_check_pb2.DependencyCheck, _Mapping]]] = ..., all_dependencies_healthy: bool = ..., healthy_count: _Optional[int] = ..., unhealthy_count: _Optional[int] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ..., issues: _Optional[_Iterable[str]] = ...) -> None: ...
