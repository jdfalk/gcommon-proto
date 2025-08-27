from gcommon.v1.common import serving_status_pb2 as _serving_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComponentHealth(_message.Message):
    __slots__ = ("name", "status", "message", "duration_ms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: _serving_status_pb2.ServingStatus
    message: str
    duration_ms: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        status: _Optional[_Union[_serving_status_pb2.ServingStatus, str]] = ...,
        message: _Optional[str] = ...,
        duration_ms: _Optional[int] = ...,
    ) -> None: ...
