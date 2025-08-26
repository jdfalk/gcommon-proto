from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PromotionRule(_message.Message):
    __slots__ = ("name", "source_environment", "target_environment", "conditions", "approval_required", "approvers", "automatic", "schedule", "filters", "transformations")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    APPROVERS_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_environment: str
    target_environment: str
    conditions: _containers.RepeatedScalarFieldContainer[str]
    approval_required: bool
    approvers: _containers.RepeatedScalarFieldContainer[str]
    automatic: bool
    schedule: str
    filters: _containers.RepeatedScalarFieldContainer[str]
    transformations: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., source_environment: _Optional[str] = ..., target_environment: _Optional[str] = ..., conditions: _Optional[_Iterable[str]] = ..., approval_required: _Optional[bool] = ..., approvers: _Optional[_Iterable[str]] = ..., automatic: _Optional[bool] = ..., schedule: _Optional[str] = ..., filters: _Optional[_Iterable[str]] = ..., transformations: _Optional[_Iterable[str]] = ...) -> None: ...
