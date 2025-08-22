from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.queue import delivery_options_pb2 as _delivery_options_pb2
from gcommon.v1.queue import queue_message_pb2 as _queue_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendMessageRequest(_message.Message):
    __slots__ = ("queue_name", "message", "delivery_options", "metadata")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    message: _queue_message_pb2.QueueMessage
    delivery_options: _delivery_options_pb2.DeliveryOptions
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, queue_name: _Optional[str] = ..., message: _Optional[_Union[_queue_message_pb2.QueueMessage, _Mapping]] = ..., delivery_options: _Optional[_Union[_delivery_options_pb2.DeliveryOptions, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
