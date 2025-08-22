from gcommon.v1.common import delivery_status_pb2 as _delivery_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendNotificationResponse(_message.Message):
    __slots__ = ("notification_id", "accepted", "status")
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    accepted: bool
    status: _delivery_status_pb2.DeliveryStatus
    def __init__(self, notification_id: _Optional[str] = ..., accepted: bool = ..., status: _Optional[_Union[_delivery_status_pb2.DeliveryStatus, str]] = ...) -> None: ...
