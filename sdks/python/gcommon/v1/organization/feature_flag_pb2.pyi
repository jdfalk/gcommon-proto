from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureFlag(_message.Message):
    __slots__ = ("name", "enabled", "description", "rollout_percentage")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    enabled: bool
    description: str
    rollout_percentage: int
    def __init__(self, name: _Optional[str] = ..., enabled: _Optional[bool] = ..., description: _Optional[str] = ..., rollout_percentage: _Optional[int] = ...) -> None: ...
