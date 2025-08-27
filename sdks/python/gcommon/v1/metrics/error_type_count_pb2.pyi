from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorTypeCount(_message.Message):
    __slots__ = ("error_type", "count", "percentage")
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    error_type: str
    count: int
    percentage: float
    def __init__(
        self,
        error_type: _Optional[str] = ...,
        count: _Optional[int] = ...,
        percentage: _Optional[float] = ...,
    ) -> None: ...
