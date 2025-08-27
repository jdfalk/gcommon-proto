from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageStateCounts(_message.Message):
    __slots__ = (
        "pending",
        "processing",
        "completed",
        "failed",
        "retrying",
        "dead_letter",
    )
    PENDING_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    RETRYING_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_FIELD_NUMBER: _ClassVar[int]
    pending: int
    processing: int
    completed: int
    failed: int
    retrying: int
    dead_letter: int
    def __init__(
        self,
        pending: _Optional[int] = ...,
        processing: _Optional[int] = ...,
        completed: _Optional[int] = ...,
        failed: _Optional[int] = ...,
        retrying: _Optional[int] = ...,
        dead_letter: _Optional[int] = ...,
    ) -> None: ...
