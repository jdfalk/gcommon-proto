import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlowControl(_message.Message):
    __slots__ = ("max_in_flight", "max_bytes_in_flight", "ack_deadline")
    MAX_IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    ACK_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    max_in_flight: int
    max_bytes_in_flight: int
    ack_deadline: _duration_pb2.Duration
    def __init__(
        self,
        max_in_flight: _Optional[int] = ...,
        max_bytes_in_flight: _Optional[int] = ...,
        ack_deadline: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
    ) -> None: ...
