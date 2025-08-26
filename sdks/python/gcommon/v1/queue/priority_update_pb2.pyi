from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PriorityUpdate(_message.Message):
    __slots__ = ("priority_level", "priority_reason", "maintain_order")
    PRIORITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_REASON_FIELD_NUMBER: _ClassVar[int]
    MAINTAIN_ORDER_FIELD_NUMBER: _ClassVar[int]
    priority_level: int
    priority_reason: str
    maintain_order: bool
    def __init__(self, priority_level: _Optional[int] = ..., priority_reason: _Optional[str] = ..., maintain_order: bool = ...) -> None: ...
