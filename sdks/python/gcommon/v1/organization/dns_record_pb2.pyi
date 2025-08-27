from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DNSRecord(_message.Message):
    __slots__ = ("type", "name", "value", "ttl", "priority")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    type: str
    name: str
    value: str
    ttl: int
    priority: int
    def __init__(
        self,
        type: _Optional[str] = ...,
        name: _Optional[str] = ...,
        value: _Optional[str] = ...,
        ttl: _Optional[int] = ...,
        priority: _Optional[int] = ...,
    ) -> None: ...
