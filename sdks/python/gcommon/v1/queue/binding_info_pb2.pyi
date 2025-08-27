from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BindingInfo(_message.Message):
    __slots__ = (
        "binding_name",
        "source",
        "destination",
        "routing_key",
        "arguments",
        "durable",
        "auto_delete",
        "binding_type",
        "created_at",
    )
    class ArgumentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    BINDING_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
    BINDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    binding_name: str
    source: str
    destination: str
    routing_key: str
    arguments: _containers.ScalarMap[str, str]
    durable: bool
    auto_delete: bool
    binding_type: str
    created_at: int
    def __init__(
        self,
        binding_name: _Optional[str] = ...,
        source: _Optional[str] = ...,
        destination: _Optional[str] = ...,
        routing_key: _Optional[str] = ...,
        arguments: _Optional[_Mapping[str, str]] = ...,
        durable: _Optional[bool] = ...,
        auto_delete: _Optional[bool] = ...,
        binding_type: _Optional[str] = ...,
        created_at: _Optional[int] = ...,
    ) -> None: ...
