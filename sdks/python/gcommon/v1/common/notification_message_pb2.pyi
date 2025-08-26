import datetime

from gcommon.v1.common import delivery_channel_pb2 as _delivery_channel_pb2
from gcommon.v1.common import delivery_status_pb2 as _delivery_status_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationMessage(_message.Message):
    __slots__ = ("id", "subject", "body", "data", "channels", "send_at", "status", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SEND_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    subject: str
    body: str
    data: _any_pb2.Any
    channels: _containers.RepeatedCompositeFieldContainer[_delivery_channel_pb2.DeliveryChannel]
    send_at: _timestamp_pb2.Timestamp
    status: _delivery_status_pb2.DeliveryStatus
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., subject: _Optional[str] = ..., body: _Optional[str] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., channels: _Optional[_Iterable[_Union[_delivery_channel_pb2.DeliveryChannel, _Mapping]]] = ..., send_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[_delivery_status_pb2.DeliveryStatus, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
