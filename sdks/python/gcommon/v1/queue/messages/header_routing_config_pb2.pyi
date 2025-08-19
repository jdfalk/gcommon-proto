from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HeaderRoutingConfig(_message.Message):
    __slots__ = ("routing_header", "exact_match", "case_sensitive")
    ROUTING_HEADER_FIELD_NUMBER: _ClassVar[int]
    EXACT_MATCH_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    routing_header: str
    exact_match: bool
    case_sensitive: bool
    def __init__(self, routing_header: _Optional[str] = ..., exact_match: bool = ..., case_sensitive: bool = ...) -> None: ...
