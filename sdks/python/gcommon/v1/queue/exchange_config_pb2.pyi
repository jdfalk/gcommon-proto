from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeConfig(_message.Message):
    __slots__ = ("name", "exchange_type", "durable", "auto_delete", "internal", "arguments", "routing_key", "alternate_exchange")
    class ArgumentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    exchange_type: str
    durable: bool
    auto_delete: bool
    internal: bool
    arguments: _containers.ScalarMap[str, str]
    routing_key: str
    alternate_exchange: str
    def __init__(self, name: _Optional[str] = ..., exchange_type: _Optional[str] = ..., durable: bool = ..., auto_delete: bool = ..., internal: bool = ..., arguments: _Optional[_Mapping[str, str]] = ..., routing_key: _Optional[str] = ..., alternate_exchange: _Optional[str] = ...) -> None: ...
