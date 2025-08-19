from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALIDATION_RESULT_TYPE_UNSPECIFIED: _ClassVar[ValidationResultType]
    VALIDATION_RESULT_TYPE_PASS: _ClassVar[ValidationResultType]
    VALIDATION_RESULT_TYPE_FAIL: _ClassVar[ValidationResultType]
    VALIDATION_RESULT_TYPE_WARNING: _ClassVar[ValidationResultType]
    VALIDATION_RESULT_TYPE_SKIP: _ClassVar[ValidationResultType]
VALIDATION_RESULT_TYPE_UNSPECIFIED: ValidationResultType
VALIDATION_RESULT_TYPE_PASS: ValidationResultType
VALIDATION_RESULT_TYPE_FAIL: ValidationResultType
VALIDATION_RESULT_TYPE_WARNING: ValidationResultType
VALIDATION_RESULT_TYPE_SKIP: ValidationResultType
