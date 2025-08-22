from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StopWorkflowRequest(_message.Message):
    __slots__ = ("execution_id", "reason")
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    reason: str
    def __init__(self, execution_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...
