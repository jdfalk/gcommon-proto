from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValueValidationSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE_VALIDATION_SEVERITY_UNSPECIFIED: _ClassVar[ValueValidationSeverity]
    VALUE_VALIDATION_SEVERITY_INFO: _ClassVar[ValueValidationSeverity]
    VALUE_VALIDATION_SEVERITY_WARNING: _ClassVar[ValueValidationSeverity]
    VALUE_VALIDATION_SEVERITY_ERROR: _ClassVar[ValueValidationSeverity]
    VALUE_VALIDATION_SEVERITY_CRITICAL: _ClassVar[ValueValidationSeverity]
VALUE_VALIDATION_SEVERITY_UNSPECIFIED: ValueValidationSeverity
VALUE_VALIDATION_SEVERITY_INFO: ValueValidationSeverity
VALUE_VALIDATION_SEVERITY_WARNING: ValueValidationSeverity
VALUE_VALIDATION_SEVERITY_ERROR: ValueValidationSeverity
VALUE_VALIDATION_SEVERITY_CRITICAL: ValueValidationSeverity
