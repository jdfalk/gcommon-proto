from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AgeBucket(_message.Message):
    __slots__ = ("min_age_seconds", "max_age_seconds", "message_count")
    MIN_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_age_seconds: int
    max_age_seconds: int
    message_count: int
    def __init__(
        self,
        min_age_seconds: _Optional[int] = ...,
        max_age_seconds: _Optional[int] = ...,
        message_count: _Optional[int] = ...,
    ) -> None: ...
