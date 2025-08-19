from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientInfo(_message.Message):
    __slots__ = ("name", "version", "ip_address", "user_agent", "platform")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    ip_address: str
    user_agent: str
    platform: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., ip_address: _Optional[str] = ..., user_agent: _Optional[str] = ..., platform: _Optional[str] = ...) -> None: ...
