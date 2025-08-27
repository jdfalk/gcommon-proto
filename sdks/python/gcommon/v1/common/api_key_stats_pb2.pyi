from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApiKeyStats(_message.Message):
    __slots__ = (
        "total_requests",
        "successful_requests",
        "failed_requests",
        "last_used_at",
    )
    TOTAL_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    FAILED_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    total_requests: int
    successful_requests: int
    failed_requests: int
    last_used_at: int
    def __init__(
        self,
        total_requests: _Optional[int] = ...,
        successful_requests: _Optional[int] = ...,
        failed_requests: _Optional[int] = ...,
        last_used_at: _Optional[int] = ...,
    ) -> None: ...
