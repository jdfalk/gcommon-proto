import datetime

from gcommon.v1.common import notification_message_pb2 as _notification_message_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventNotification(_message.Message):
    __slots__ = (
        "event_id",
        "event_type",
        "event_payload",
        "notification",
        "event_time",
    )
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    event_type: str
    event_payload: _any_pb2.Any
    notification: _notification_message_pb2.NotificationMessage
    event_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        event_id: _Optional[str] = ...,
        event_type: _Optional[str] = ...,
        event_payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...,
        notification: _Optional[
            _Union[_notification_message_pb2.NotificationMessage, _Mapping]
        ] = ...,
        event_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
