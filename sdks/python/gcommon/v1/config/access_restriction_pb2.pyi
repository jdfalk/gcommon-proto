from gcommon.v1.common import restriction_type_pb2 as _restriction_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessRestriction(_message.Message):
    __slots__ = ("type", "value", "operator", "reason")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    type: _restriction_type_pb2.RestrictionType
    value: str
    operator: str
    reason: str
    def __init__(self, type: _Optional[_Union[_restriction_type_pb2.RestrictionType, str]] = ..., value: _Optional[str] = ..., operator: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...
