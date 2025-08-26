from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RemediationDetails(_message.Message):
    __slots__ = ("action_type", "description", "auto_remediation_enabled", "max_attempts", "current_attempts", "last_attempt_timestamp", "success", "error_message")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTO_REMEDIATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    LAST_ATTEMPT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    action_type: str
    description: str
    auto_remediation_enabled: bool
    max_attempts: int
    current_attempts: int
    last_attempt_timestamp: int
    success: bool
    error_message: str
    def __init__(self, action_type: _Optional[str] = ..., description: _Optional[str] = ..., auto_remediation_enabled: _Optional[bool] = ..., max_attempts: _Optional[int] = ..., current_attempts: _Optional[int] = ..., last_attempt_timestamp: _Optional[int] = ..., success: _Optional[bool] = ..., error_message: _Optional[str] = ...) -> None: ...
