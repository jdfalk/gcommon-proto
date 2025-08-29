from gcommon.v1.health.messages import health_check_pb2 as _health_check_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterCheckRequest(_message.Message):
    __slots__ = ("health_check", "metadata", "replace_existing")
    HEALTH_CHECK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    health_check: _health_check_pb2.HealthCheck
    metadata: _request_metadata_pb2.RequestMetadata
    replace_existing: bool
    def __init__(self, health_check: _Optional[_Union[_health_check_pb2.HealthCheck, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., replace_existing: bool = ...) -> None: ...
