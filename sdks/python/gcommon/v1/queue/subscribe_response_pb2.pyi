from gcommon.v1.queue import connection_details_pb2 as _connection_details_pb2
from gcommon.v1.queue import partition_offset_pb2 as _partition_offset_pb2
from gcommon.v1.queue import queue_message_pb2 as _queue_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscribeResponse(_message.Message):
    __slots__ = (
        "message",
        "partition_offset",
        "connection_details",
        "subscription_id",
        "error",
    )
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    message: _queue_message_pb2.QueueMessage
    partition_offset: _partition_offset_pb2.PartitionOffset
    connection_details: _connection_details_pb2.ConnectionDetails
    subscription_id: str
    error: str
    def __init__(
        self,
        message: _Optional[_Union[_queue_message_pb2.QueueMessage, _Mapping]] = ...,
        partition_offset: _Optional[
            _Union[_partition_offset_pb2.PartitionOffset, _Mapping]
        ] = ...,
        connection_details: _Optional[
            _Union[_connection_details_pb2.ConnectionDetails, _Mapping]
        ] = ...,
        subscription_id: _Optional[str] = ...,
        error: _Optional[str] = ...,
    ) -> None: ...
