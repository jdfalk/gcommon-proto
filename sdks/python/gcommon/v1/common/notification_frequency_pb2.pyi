from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationFrequency(_message.Message):
    __slots__ = (
        "daily_digest",
        "weekly_summary",
        "instant_notifications",
        "quiet_hours_start",
        "quiet_hours_end",
    )
    DAILY_DIGEST_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    INSTANT_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    QUIET_HOURS_START_FIELD_NUMBER: _ClassVar[int]
    QUIET_HOURS_END_FIELD_NUMBER: _ClassVar[int]
    daily_digest: bool
    weekly_summary: bool
    instant_notifications: bool
    quiet_hours_start: str
    quiet_hours_end: str
    def __init__(
        self,
        daily_digest: _Optional[bool] = ...,
        weekly_summary: _Optional[bool] = ...,
        instant_notifications: _Optional[bool] = ...,
        quiet_hours_start: _Optional[str] = ...,
        quiet_hours_end: _Optional[str] = ...,
    ) -> None: ...
