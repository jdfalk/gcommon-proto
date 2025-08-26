from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApprovalRequirement(_message.Message):
    __slots__ = ("required", "approval_count", "approver_roles", "approver_users", "policy", "workflow", "auto_approval_conditions", "approval_timeout_hours")
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    APPROVER_ROLES_FIELD_NUMBER: _ClassVar[int]
    APPROVER_USERS_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVAL_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_TIMEOUT_HOURS_FIELD_NUMBER: _ClassVar[int]
    required: bool
    approval_count: int
    approver_roles: _containers.RepeatedScalarFieldContainer[str]
    approver_users: _containers.RepeatedScalarFieldContainer[str]
    policy: str
    workflow: str
    auto_approval_conditions: _containers.RepeatedScalarFieldContainer[str]
    approval_timeout_hours: int
    def __init__(self, required: _Optional[bool] = ..., approval_count: _Optional[int] = ..., approver_roles: _Optional[_Iterable[str]] = ..., approver_users: _Optional[_Iterable[str]] = ..., policy: _Optional[str] = ..., workflow: _Optional[str] = ..., auto_approval_conditions: _Optional[_Iterable[str]] = ..., approval_timeout_hours: _Optional[int] = ...) -> None: ...
