from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationRuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALIDATION_RULE_TYPE_UNSPECIFIED: _ClassVar[ValidationRuleType]
    VALIDATION_RULE_TYPE_REGEX: _ClassVar[ValidationRuleType]
    VALIDATION_RULE_TYPE_RANGE: _ClassVar[ValidationRuleType]
    VALIDATION_RULE_TYPE_LENGTH: _ClassVar[ValidationRuleType]
    VALIDATION_RULE_TYPE_FORMAT: _ClassVar[ValidationRuleType]
    VALIDATION_RULE_TYPE_ENUM: _ClassVar[ValidationRuleType]
    VALIDATION_RULE_TYPE_CUSTOM: _ClassVar[ValidationRuleType]
    VALIDATION_RULE_TYPE_FUNCTION: _ClassVar[ValidationRuleType]
    VALIDATION_RULE_TYPE_SCHEMA: _ClassVar[ValidationRuleType]
VALIDATION_RULE_TYPE_UNSPECIFIED: ValidationRuleType
VALIDATION_RULE_TYPE_REGEX: ValidationRuleType
VALIDATION_RULE_TYPE_RANGE: ValidationRuleType
VALIDATION_RULE_TYPE_LENGTH: ValidationRuleType
VALIDATION_RULE_TYPE_FORMAT: ValidationRuleType
VALIDATION_RULE_TYPE_ENUM: ValidationRuleType
VALIDATION_RULE_TYPE_CUSTOM: ValidationRuleType
VALIDATION_RULE_TYPE_FUNCTION: ValidationRuleType
VALIDATION_RULE_TYPE_SCHEMA: ValidationRuleType
