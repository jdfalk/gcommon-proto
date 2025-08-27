from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALIDATION_SEVERITY_UNSPECIFIED: _ClassVar[ValidationSeverity]
    VALIDATION_SEVERITY_INFO: _ClassVar[ValidationSeverity]
    VALIDATION_SEVERITY_WARNING: _ClassVar[ValidationSeverity]
    VALIDATION_SEVERITY_ERROR: _ClassVar[ValidationSeverity]
    VALIDATION_SEVERITY_CRITICAL: _ClassVar[ValidationSeverity]

VALIDATION_SEVERITY_UNSPECIFIED: ValidationSeverity
VALIDATION_SEVERITY_INFO: ValidationSeverity
VALIDATION_SEVERITY_WARNING: ValidationSeverity
VALIDATION_SEVERITY_ERROR: ValidationSeverity
VALIDATION_SEVERITY_CRITICAL: ValidationSeverity
