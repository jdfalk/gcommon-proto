import datetime

from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerEvent(_message.Message):
    __slots__ = ("event_type", "event_data", "server_id", "metadata", "event_time")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    event_data: _any_pb2.Any
    server_id: str
    metadata: str
    event_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        event_type: _Optional[str] = ...,
        event_data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...,
        server_id: _Optional[str] = ...,
        metadata: _Optional[str] = ...,
        event_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
