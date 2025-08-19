from gcommon.v1.config.enums import validation_result_type_pb2 as _validation_result_type_pb2
from gcommon.v1.config.enums import validation_severity_pb2 as _validation_severity_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigValidationResult(_message.Message):
    __slots__ = ("rule_name", "result", "message", "severity", "field", "context")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    rule_name: str
    result: _validation_result_type_pb2.ValidationResultType
    message: str
    severity: _validation_severity_pb2.ValidationSeverity
    field: str
    context: _containers.ScalarMap[str, str]
    def __init__(self, rule_name: _Optional[str] = ..., result: _Optional[_Union[_validation_result_type_pb2.ValidationResultType, str]] = ..., message: _Optional[str] = ..., severity: _Optional[_Union[_validation_severity_pb2.ValidationSeverity, str]] = ..., field: _Optional[str] = ..., context: _Optional[_Mapping[str, str]] = ...) -> None: ...
