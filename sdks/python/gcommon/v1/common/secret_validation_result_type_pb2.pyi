from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SecretValidationResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECRET_VALIDATION_RESULT_TYPE_UNSPECIFIED: _ClassVar[SecretValidationResultType]
    SECRET_VALIDATION_RESULT_TYPE_PASS: _ClassVar[SecretValidationResultType]
    SECRET_VALIDATION_RESULT_TYPE_FAIL: _ClassVar[SecretValidationResultType]
    SECRET_VALIDATION_RESULT_TYPE_WARNING: _ClassVar[SecretValidationResultType]
    SECRET_VALIDATION_RESULT_TYPE_SKIP: _ClassVar[SecretValidationResultType]
SECRET_VALIDATION_RESULT_TYPE_UNSPECIFIED: SecretValidationResultType
SECRET_VALIDATION_RESULT_TYPE_PASS: SecretValidationResultType
SECRET_VALIDATION_RESULT_TYPE_FAIL: SecretValidationResultType
SECRET_VALIDATION_RESULT_TYPE_WARNING: SecretValidationResultType
SECRET_VALIDATION_RESULT_TYPE_SKIP: SecretValidationResultType
