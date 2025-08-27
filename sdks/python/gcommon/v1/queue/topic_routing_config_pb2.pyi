from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TopicRoutingConfig(_message.Message):
    __slots__ = ("exchange_name", "default_routing_key", "wildcard_matching")
    EXCHANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    WILDCARD_MATCHING_FIELD_NUMBER: _ClassVar[int]
    exchange_name: str
    default_routing_key: str
    wildcard_matching: bool
    def __init__(
        self,
        exchange_name: _Optional[str] = ...,
        default_routing_key: _Optional[str] = ...,
        wildcard_matching: _Optional[bool] = ...,
    ) -> None: ...
