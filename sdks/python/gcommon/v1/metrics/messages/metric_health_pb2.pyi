from gcommon.v1.common.enums import health_status_pb2 as _health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricHealth(_message.Message):
    __slots__ = ("target_id", "status", "checked_at", "message")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    status: _health_status_pb2.CommonHealthStatus
    checked_at: _timestamp_pb2.Timestamp
    message: str
    def __init__(self, target_id: _Optional[str] = ..., status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., checked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...
