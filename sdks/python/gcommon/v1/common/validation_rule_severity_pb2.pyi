from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationRuleSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALIDATION_RULE_SEVERITY_UNSPECIFIED: _ClassVar[ValidationRuleSeverity]
    VALIDATION_RULE_SEVERITY_INFO: _ClassVar[ValidationRuleSeverity]
    VALIDATION_RULE_SEVERITY_WARNING: _ClassVar[ValidationRuleSeverity]
    VALIDATION_RULE_SEVERITY_ERROR: _ClassVar[ValidationRuleSeverity]
    VALIDATION_RULE_SEVERITY_CRITICAL: _ClassVar[ValidationRuleSeverity]

VALIDATION_RULE_SEVERITY_UNSPECIFIED: ValidationRuleSeverity
VALIDATION_RULE_SEVERITY_INFO: ValidationRuleSeverity
VALIDATION_RULE_SEVERITY_WARNING: ValidationRuleSeverity
VALIDATION_RULE_SEVERITY_ERROR: ValidationRuleSeverity
VALIDATION_RULE_SEVERITY_CRITICAL: ValidationRuleSeverity
