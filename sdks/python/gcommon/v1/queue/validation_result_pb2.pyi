from gcommon.v1.queue import checksum_validation_pb2 as _checksum_validation_pb2
from gcommon.v1.queue import integrity_validation_pb2 as _integrity_validation_pb2
from gcommon.v1.queue import schema_validation_pb2 as _schema_validation_pb2
from gcommon.v1.queue import validation_error_pb2 as _validation_error_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueValidationResult(_message.Message):
    __slots__ = ("validation_passed", "checksum_validation", "schema_validation", "integrity_validation", "validation_errors", "validation_duration")
    VALIDATION_PASSED_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    INTEGRITY_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    validation_passed: bool
    checksum_validation: _checksum_validation_pb2.ChecksumValidation
    schema_validation: _schema_validation_pb2.SchemaValidation
    integrity_validation: _integrity_validation_pb2.IntegrityValidation
    validation_errors: _containers.RepeatedCompositeFieldContainer[_validation_error_pb2.ValidationError]
    validation_duration: _duration_pb2.Duration
    def __init__(self, validation_passed: bool = ..., checksum_validation: _Optional[_Union[_checksum_validation_pb2.ChecksumValidation, _Mapping]] = ..., schema_validation: _Optional[_Union[_schema_validation_pb2.SchemaValidation, _Mapping]] = ..., integrity_validation: _Optional[_Union[_integrity_validation_pb2.IntegrityValidation, _Mapping]] = ..., validation_errors: _Optional[_Iterable[_Union[_validation_error_pb2.ValidationError, _Mapping]]] = ..., validation_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
