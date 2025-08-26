from gcommon.v1.config import approval_stage_pb2 as _approval_stage_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApprovalWorkflow(_message.Message):
    __slots__ = ("enabled", "type", "stages", "timeout_hours", "conditions", "notifications")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_HOURS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    type: str
    stages: _containers.RepeatedCompositeFieldContainer[_approval_stage_pb2.ApprovalStage]
    timeout_hours: int
    conditions: _containers.RepeatedScalarFieldContainer[str]
    notifications: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enabled: _Optional[bool] = ..., type: _Optional[str] = ..., stages: _Optional[_Iterable[_Union[_approval_stage_pb2.ApprovalStage, _Mapping]]] = ..., timeout_hours: _Optional[int] = ..., conditions: _Optional[_Iterable[str]] = ..., notifications: _Optional[_Iterable[str]] = ...) -> None: ...
