from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MultiValueConfig(_message.Message):
    __slots__ = ("max_values", "value_ttl_seconds", "cleanup_strategy")
    MAX_VALUES_FIELD_NUMBER: _ClassVar[int]
    VALUE_TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    max_values: int
    value_ttl_seconds: int
    cleanup_strategy: str
    def __init__(self, max_values: _Optional[int] = ..., value_ttl_seconds: _Optional[int] = ..., cleanup_strategy: _Optional[str] = ...) -> None: ...
