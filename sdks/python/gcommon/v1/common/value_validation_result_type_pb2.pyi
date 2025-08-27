from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValueValidationResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE_VALIDATION_RESULT_TYPE_UNSPECIFIED: _ClassVar[ValueValidationResultType]
    VALUE_VALIDATION_RESULT_TYPE_PASS: _ClassVar[ValueValidationResultType]
    VALUE_VALIDATION_RESULT_TYPE_FAIL: _ClassVar[ValueValidationResultType]
    VALUE_VALIDATION_RESULT_TYPE_WARNING: _ClassVar[ValueValidationResultType]
    VALUE_VALIDATION_RESULT_TYPE_SKIP: _ClassVar[ValueValidationResultType]

VALUE_VALIDATION_RESULT_TYPE_UNSPECIFIED: ValueValidationResultType
VALUE_VALIDATION_RESULT_TYPE_PASS: ValueValidationResultType
VALUE_VALIDATION_RESULT_TYPE_FAIL: ValueValidationResultType
VALUE_VALIDATION_RESULT_TYPE_WARNING: ValueValidationResultType
VALUE_VALIDATION_RESULT_TYPE_SKIP: ValueValidationResultType
