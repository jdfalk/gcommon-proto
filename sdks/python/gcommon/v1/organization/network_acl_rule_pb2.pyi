from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkACLRule(_message.Message):
    __slots__ = ("action", "source", "destination", "protocol", "port_range", "priority")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PORT_RANGE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    action: str
    source: str
    destination: str
    protocol: str
    port_range: str
    priority: int
    def __init__(self, action: _Optional[str] = ..., source: _Optional[str] = ..., destination: _Optional[str] = ..., protocol: _Optional[str] = ..., port_range: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...
