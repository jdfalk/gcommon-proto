from gcommon.v1.common import value_validation_result_type_pb2 as _value_validation_result_type_pb2
from gcommon.v1.common import value_validation_severity_pb2 as _value_validation_severity_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValueValidationResult(_message.Message):
    __slots__ = ("name", "result", "message", "severity", "timestamp", "details", "rule", "context")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    result: _value_validation_result_type_pb2.ValueValidationResultType
    message: str
    severity: _value_validation_severity_pb2.ValueValidationSeverity
    timestamp: _timestamp_pb2.Timestamp
    details: _containers.ScalarMap[str, str]
    rule: str
    context: str
    def __init__(self, name: _Optional[str] = ..., result: _Optional[_Union[_value_validation_result_type_pb2.ValueValidationResultType, str]] = ..., message: _Optional[str] = ..., severity: _Optional[_Union[_value_validation_severity_pb2.ValueValidationSeverity, str]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., details: _Optional[_Mapping[str, str]] = ..., rule: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...
