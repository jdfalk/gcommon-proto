from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueueMonitoringConfig(_message.Message):
    __slots__ = ("enabled", "metrics_endpoint")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    METRICS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    metrics_endpoint: str
    def __init__(self, enabled: bool = ..., metrics_endpoint: _Optional[str] = ...) -> None: ...
