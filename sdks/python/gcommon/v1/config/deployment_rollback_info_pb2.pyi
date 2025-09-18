import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentRollbackInfo(_message.Message):
    __slots__ = ("available", "previous_version", "rollback_timestamp", "reason", "method")
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VERSION_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    available: bool
    previous_version: str
    rollback_timestamp: _timestamp_pb2.Timestamp
    reason: str
    method: str
    def __init__(self, available: _Optional[bool] = ..., previous_version: _Optional[str] = ..., rollback_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reason: _Optional[str] = ..., method: _Optional[str] = ...) -> None: ...
