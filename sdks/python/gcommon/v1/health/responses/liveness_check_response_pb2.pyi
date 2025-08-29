from gcommon.v1.health.enums import health_status_pb2 as _health_status_pb2
from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessCheckResponse(_message.Message):
    __slots__ = ("status", "alive", "started_at", "metadata", "details")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    status: _health_status_pb2.HealthStatus
    alive: bool
    started_at: _timestamp_pb2.Timestamp
    metadata: _response_metadata_pb2.ResponseMetadata
    details: str
    def __init__(self, status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., alive: bool = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ..., details: _Optional[str] = ...) -> None: ...
