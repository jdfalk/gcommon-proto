from gcommon.v1.common import parameter_constraints_pb2 as _parameter_constraints_pb2
from gcommon.v1.common import parameter_type_pb2 as _parameter_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateParameter(_message.Message):
    __slots__ = ("name", "description", "type", "required", "default_value", "allowed_values", "constraints", "group", "order", "sensitive", "validation_pattern", "examples", "documentation", "display_name", "placeholder")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_PATTERN_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    type: _parameter_type_pb2.ParameterType
    required: bool
    default_value: str
    allowed_values: _containers.RepeatedScalarFieldContainer[str]
    constraints: _parameter_constraints_pb2.ParameterConstraints
    group: str
    order: int
    sensitive: bool
    validation_pattern: str
    examples: _containers.RepeatedScalarFieldContainer[str]
    documentation: str
    display_name: str
    placeholder: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_parameter_type_pb2.ParameterType, str]] = ..., required: _Optional[bool] = ..., default_value: _Optional[str] = ..., allowed_values: _Optional[_Iterable[str]] = ..., constraints: _Optional[_Union[_parameter_constraints_pb2.ParameterConstraints, _Mapping]] = ..., group: _Optional[str] = ..., order: _Optional[int] = ..., sensitive: _Optional[bool] = ..., validation_pattern: _Optional[str] = ..., examples: _Optional[_Iterable[str]] = ..., documentation: _Optional[str] = ..., display_name: _Optional[str] = ..., placeholder: _Optional[str] = ...) -> None: ...
