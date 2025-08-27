from gcommon.v1.common import health_check_request_pb2 as _health_check_request_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterCheckRequest(_message.Message):
    __slots__ = ("service", "check", "metadata")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    CHECK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    service: str
    check: _health_check_request_pb2.HealthHealthCheckRequest
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(
        self,
        service: _Optional[str] = ...,
        check: _Optional[
            _Union[_health_check_request_pb2.HealthHealthCheckRequest, _Mapping]
        ] = ...,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
    ) -> None: ...
