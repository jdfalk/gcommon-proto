from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ComplianceReporting(_message.Message):
    __slots__ = ("enabled", "frequency_hours", "recipients")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_HOURS_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    frequency_hours: int
    recipients: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enabled: bool = ..., frequency_hours: _Optional[int] = ..., recipients: _Optional[_Iterable[str]] = ...) -> None: ...
