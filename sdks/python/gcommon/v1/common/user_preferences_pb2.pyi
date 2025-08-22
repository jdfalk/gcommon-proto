from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserPreferences(_message.Message):
    __slots__ = ("email_notifications", "sms_notifications", "push_notifications", "marketing_emails", "two_factor_enabled", "session_timeout_minutes", "theme")
    EMAIL_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    SMS_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    PUSH_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    MARKETING_EMAILS_FIELD_NUMBER: _ClassVar[int]
    TWO_FACTOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SESSION_TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    email_notifications: bool
    sms_notifications: bool
    push_notifications: bool
    marketing_emails: bool
    two_factor_enabled: bool
    session_timeout_minutes: int
    theme: str
    def __init__(self, email_notifications: bool = ..., sms_notifications: bool = ..., push_notifications: bool = ..., marketing_emails: bool = ..., two_factor_enabled: bool = ..., session_timeout_minutes: _Optional[int] = ..., theme: _Optional[str] = ...) -> None: ...
