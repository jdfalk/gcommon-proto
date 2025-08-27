import datetime

from gcommon.v1.common import secret_validation_result_type_pb2 as _secret_validation_result_type_pb2
from gcommon.v1.common import secret_validation_severity_pb2 as _secret_validation_severity_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecretValidationResult(_message.Message):
    __slots__ = ("name", "result", "message", "severity", "timestamp", "details")
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
    name: str
    result: _secret_validation_result_type_pb2.SecretValidationResultType
    message: str
    severity: _secret_validation_severity_pb2.SecretValidationSeverity
    timestamp: _timestamp_pb2.Timestamp
    details: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., result: _Optional[_Union[_secret_validation_result_type_pb2.SecretValidationResultType, str]] = ..., message: _Optional[str] = ..., severity: _Optional[_Union[_secret_validation_severity_pb2.SecretValidationSeverity, str]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., details: _Optional[_Mapping[str, str]] = ...) -> None: ...
