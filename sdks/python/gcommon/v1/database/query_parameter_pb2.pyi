from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParameter(_message.Message):
    __slots__ = ("name", "value", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _any_pb2.Any
    type: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., type: _Optional[str] = ...) -> None: ...
