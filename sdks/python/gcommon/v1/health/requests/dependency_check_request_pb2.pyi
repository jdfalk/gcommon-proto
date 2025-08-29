from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DependencyCheckRequest(_message.Message):
    __slots__ = ("service_name", "dependency_name", "metadata", "timeout", "critical_only", "min_criticality")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_ONLY_FIELD_NUMBER: _ClassVar[int]
    MIN_CRITICALITY_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    dependency_name: str
    metadata: _request_metadata_pb2.RequestMetadata
    timeout: _duration_pb2.Duration
    critical_only: bool
    min_criticality: int
    def __init__(self, service_name: _Optional[str] = ..., dependency_name: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., critical_only: bool = ..., min_criticality: _Optional[int] = ...) -> None: ...
