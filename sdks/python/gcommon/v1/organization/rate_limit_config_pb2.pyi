from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationRateLimitConfig(_message.Message):
    __slots__ = ("requests_per_minute", "requests_per_hour", "requests_per_day")
    REQUESTS_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_PER_DAY_FIELD_NUMBER: _ClassVar[int]
    requests_per_minute: int
    requests_per_hour: int
    requests_per_day: int
    def __init__(
        self,
        requests_per_minute: _Optional[int] = ...,
        requests_per_hour: _Optional[int] = ...,
        requests_per_day: _Optional[int] = ...,
    ) -> None: ...
