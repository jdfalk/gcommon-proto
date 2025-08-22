from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VersionQualityIssue(_message.Message):
    __slots__ = ("type", "severity", "description", "location", "rule", "fix_suggestion")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    FIX_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    type: str
    severity: str
    description: str
    location: str
    rule: str
    fix_suggestion: str
    def __init__(self, type: _Optional[str] = ..., severity: _Optional[str] = ..., description: _Optional[str] = ..., location: _Optional[str] = ..., rule: _Optional[str] = ..., fix_suggestion: _Optional[str] = ...) -> None: ...
