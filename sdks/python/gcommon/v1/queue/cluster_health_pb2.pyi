from gcommon.v1.common import health_status_pb2 as _health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterHealth(_message.Message):
    __slots__ = ("status", "healthy_nodes", "total_nodes", "issues")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_NODES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NODES_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    status: _health_status_pb2.CommonHealthStatus
    healthy_nodes: int
    total_nodes: int
    issues: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., healthy_nodes: _Optional[int] = ..., total_nodes: _Optional[int] = ..., issues: _Optional[_Iterable[str]] = ...) -> None: ...
