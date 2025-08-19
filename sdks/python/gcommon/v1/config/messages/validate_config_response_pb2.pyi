from gcommon.v1.config.messages import config_validation_error_pb2 as _config_validation_error_pb2
from gcommon.v1.config.messages import config_validation_warning_pb2 as _config_validation_warning_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateConfigResponse(_message.Message):
    __slots__ = ("valid", "errors", "warnings")
    VALID_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    errors: _containers.RepeatedCompositeFieldContainer[_config_validation_error_pb2.ConfigValidationError]
    warnings: _containers.RepeatedCompositeFieldContainer[_config_validation_warning_pb2.ConfigValidationWarning]
    def __init__(self, valid: bool = ..., errors: _Optional[_Iterable[_Union[_config_validation_error_pb2.ConfigValidationError, _Mapping]]] = ..., warnings: _Optional[_Iterable[_Union[_config_validation_warning_pb2.ConfigValidationWarning, _Mapping]]] = ...) -> None: ...
