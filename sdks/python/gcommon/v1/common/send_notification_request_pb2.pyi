from gcommon.v1.common import notification_message_pb2 as _notification_message_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendNotificationRequest(_message.Message):
    __slots__ = ("metadata", "notification")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    notification: _notification_message_pb2.NotificationMessage
    def __init__(
        self,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
        notification: _Optional[
            _Union[_notification_message_pb2.NotificationMessage, _Mapping]
        ] = ...,
    ) -> None: ...
