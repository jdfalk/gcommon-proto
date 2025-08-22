from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PushResponse(_message.Message):
    __slots__ = ("message_id", "accepted_at", "message_offset", "queue_depth", "persisted", "estimated_delivery_time")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    QUEUE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    PERSISTED_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DELIVERY_TIME_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    accepted_at: _timestamp_pb2.Timestamp
    message_offset: int
    queue_depth: int
    persisted: bool
    estimated_delivery_time: _timestamp_pb2.Timestamp
    def __init__(self, message_id: _Optional[str] = ..., accepted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message_offset: _Optional[int] = ..., queue_depth: _Optional[int] = ..., persisted: bool = ..., estimated_delivery_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
