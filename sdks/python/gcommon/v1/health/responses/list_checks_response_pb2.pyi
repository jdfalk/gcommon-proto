from gcommon.v1.health.messages import health_check_pb2 as _health_check_pb2
from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListChecksResponse(_message.Message):
    __slots__ = ("checks", "total_count", "metadata")
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    checks: _containers.RepeatedCompositeFieldContainer[_health_check_pb2.HealthCheck]
    total_count: int
    metadata: _response_metadata_pb2.ResponseMetadata
    def __init__(self, checks: _Optional[_Iterable[_Union[_health_check_pb2.HealthCheck, _Mapping]]] = ..., total_count: _Optional[int] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...
