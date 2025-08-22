from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingConfig(_message.Message):
    __slots__ = ("strategy", "key_pattern", "sticky", "load_balancer")
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    KEY_PATTERN_FIELD_NUMBER: _ClassVar[int]
    STICKY_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_FIELD_NUMBER: _ClassVar[int]
    strategy: str
    key_pattern: str
    sticky: bool
    load_balancer: str
    def __init__(self, strategy: _Optional[str] = ..., key_pattern: _Optional[str] = ..., sticky: bool = ..., load_balancer: _Optional[str] = ...) -> None: ...
