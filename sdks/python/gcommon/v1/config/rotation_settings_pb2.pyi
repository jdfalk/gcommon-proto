from gcommon.v1.common import rotation_frequency_pb2 as _rotation_frequency_pb2
from gcommon.v1.config import rotation_event_pb2 as _rotation_event_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RotationSettings(_message.Message):
    __slots__ = ("enabled", "frequency", "schedule", "grace_period_days", "auto_rotate", "notification_recipients", "workflow", "last_rotated_at", "next_rotation_at", "rotation_history")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    GRACE_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    AUTO_ROTATE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    LAST_ROTATED_AT_FIELD_NUMBER: _ClassVar[int]
    NEXT_ROTATION_AT_FIELD_NUMBER: _ClassVar[int]
    ROTATION_HISTORY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    frequency: _rotation_frequency_pb2.RotationFrequency
    schedule: str
    grace_period_days: int
    auto_rotate: bool
    notification_recipients: _containers.RepeatedScalarFieldContainer[str]
    workflow: str
    last_rotated_at: _timestamp_pb2.Timestamp
    next_rotation_at: _timestamp_pb2.Timestamp
    rotation_history: _containers.RepeatedCompositeFieldContainer[_rotation_event_pb2.RotationEvent]
    def __init__(self, enabled: bool = ..., frequency: _Optional[_Union[_rotation_frequency_pb2.RotationFrequency, str]] = ..., schedule: _Optional[str] = ..., grace_period_days: _Optional[int] = ..., auto_rotate: bool = ..., notification_recipients: _Optional[_Iterable[str]] = ..., workflow: _Optional[str] = ..., last_rotated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_rotation_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rotation_history: _Optional[_Iterable[_Union[_rotation_event_pb2.RotationEvent, _Mapping]]] = ...) -> None: ...
