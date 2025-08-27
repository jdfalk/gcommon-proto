from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SecretValidationSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECRET_VALIDATION_SEVERITY_UNSPECIFIED: _ClassVar[SecretValidationSeverity]
    SECRET_VALIDATION_SEVERITY_INFO: _ClassVar[SecretValidationSeverity]
    SECRET_VALIDATION_SEVERITY_WARNING: _ClassVar[SecretValidationSeverity]
    SECRET_VALIDATION_SEVERITY_ERROR: _ClassVar[SecretValidationSeverity]
    SECRET_VALIDATION_SEVERITY_CRITICAL: _ClassVar[SecretValidationSeverity]
SECRET_VALIDATION_SEVERITY_UNSPECIFIED: SecretValidationSeverity
SECRET_VALIDATION_SEVERITY_INFO: SecretValidationSeverity
SECRET_VALIDATION_SEVERITY_WARNING: SecretValidationSeverity
SECRET_VALIDATION_SEVERITY_ERROR: SecretValidationSeverity
SECRET_VALIDATION_SEVERITY_CRITICAL: SecretValidationSeverity
