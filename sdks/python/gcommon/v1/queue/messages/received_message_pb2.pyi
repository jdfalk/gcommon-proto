from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReceivedMessage(_message.Message):
    __slots__ = ("id", "data", "attributes", "receive_timestamp", "ack_id")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ACK_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: bytes
    attributes: _containers.ScalarMap[str, str]
    receive_timestamp: int
    ack_id: str
    def __init__(self, id: _Optional[str] = ..., data: _Optional[bytes] = ..., attributes: _Optional[_Mapping[str, str]] = ..., receive_timestamp: _Optional[int] = ..., ack_id: _Optional[str] = ...) -> None: ...
