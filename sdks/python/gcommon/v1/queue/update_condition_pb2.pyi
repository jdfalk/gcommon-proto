from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateCondition(_message.Message):
    __slots__ = ("expected_version", "expected_state", "max_age_seconds", "only_if_not_delivered", "only_if_visible", "condition_expression")
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_STATE_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ONLY_IF_NOT_DELIVERED_FIELD_NUMBER: _ClassVar[int]
    ONLY_IF_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    expected_version: str
    expected_state: str
    max_age_seconds: int
    only_if_not_delivered: bool
    only_if_visible: bool
    condition_expression: str
    def __init__(self, expected_version: _Optional[str] = ..., expected_state: _Optional[str] = ..., max_age_seconds: _Optional[int] = ..., only_if_not_delivered: _Optional[bool] = ..., only_if_visible: _Optional[bool] = ..., condition_expression: _Optional[str] = ...) -> None: ...
