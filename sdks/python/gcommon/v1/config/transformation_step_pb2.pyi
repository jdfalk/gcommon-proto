from gcommon.v1.common import transformation_type_pb2 as _transformation_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransformationStep(_message.Message):
    __slots__ = ("name", "type", "expression", "parameters", "enabled", "order")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _transformation_type_pb2.TransformationType
    expression: str
    parameters: _containers.ScalarMap[str, str]
    enabled: bool
    order: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_transformation_type_pb2.TransformationType, str]] = ..., expression: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ..., enabled: _Optional[bool] = ..., order: _Optional[int] = ...) -> None: ...
