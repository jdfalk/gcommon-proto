from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FlowControlSettings(_message.Message):
    __slots__ = ("max_outstanding_messages", "max_outstanding_bytes", "algorithm")
    MAX_OUTSTANDING_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTSTANDING_BYTES_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    max_outstanding_messages: int
    max_outstanding_bytes: int
    algorithm: str
    def __init__(self, max_outstanding_messages: _Optional[int] = ..., max_outstanding_bytes: _Optional[int] = ..., algorithm: _Optional[str] = ...) -> None: ...
