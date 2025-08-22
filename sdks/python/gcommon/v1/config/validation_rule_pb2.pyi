from gcommon.v1.config import validation_severity_pb2 as _validation_severity_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationRule(_message.Message):
    __slots__ = ("name", "description", "expression", "error_message", "severity", "parameters", "conditions")
    class ConditionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    expression: str
    error_message: str
    severity: _validation_severity_pb2.ValidationSeverity
    parameters: _containers.RepeatedScalarFieldContainer[str]
    conditions: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., expression: _Optional[str] = ..., error_message: _Optional[str] = ..., severity: _Optional[_Union[_validation_severity_pb2.ValidationSeverity, str]] = ..., parameters: _Optional[_Iterable[str]] = ..., conditions: _Optional[_Mapping[str, str]] = ...) -> None: ...
