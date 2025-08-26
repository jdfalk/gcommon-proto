from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebsocketMessage(_message.Message):
    __slots__ = ("connection_id", "data", "message_type", "sent_at")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    data: bytes
    message_type: str
    sent_at: _timestamp_pb2.Timestamp
    def __init__(self, connection_id: _Optional[str] = ..., data: _Optional[bytes] = ..., message_type: _Optional[str] = ..., sent_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
