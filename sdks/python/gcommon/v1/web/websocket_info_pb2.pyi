from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebsocketInfo(_message.Message):
    __slots__ = ("connection_id", "client_ip", "user_agent", "connected_at")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    client_ip: str
    user_agent: str
    connected_at: _timestamp_pb2.Timestamp
    def __init__(self, connection_id: _Optional[str] = ..., client_ip: _Optional[str] = ..., user_agent: _Optional[str] = ..., connected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
