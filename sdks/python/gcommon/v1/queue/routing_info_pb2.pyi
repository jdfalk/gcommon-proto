from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingInfo(_message.Message):
    __slots__ = ("routing_key", "partition_id", "partition_key", "exchange_name", "routing_tags")
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTING_TAGS_FIELD_NUMBER: _ClassVar[int]
    routing_key: str
    partition_id: int
    partition_key: str
    exchange_name: str
    routing_tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, routing_key: _Optional[str] = ..., partition_id: _Optional[int] = ..., partition_key: _Optional[str] = ..., exchange_name: _Optional[str] = ..., routing_tags: _Optional[_Iterable[str]] = ...) -> None: ...
