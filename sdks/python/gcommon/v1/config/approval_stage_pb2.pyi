from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApprovalStage(_message.Message):
    __slots__ = ("name", "approvers", "required_approvals", "conditions", "timeout_hours", "order")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPROVERS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APPROVALS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_HOURS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    approvers: _containers.RepeatedScalarFieldContainer[str]
    required_approvals: int
    conditions: _containers.RepeatedScalarFieldContainer[str]
    timeout_hours: int
    order: int
    def __init__(self, name: _Optional[str] = ..., approvers: _Optional[_Iterable[str]] = ..., required_approvals: _Optional[int] = ..., conditions: _Optional[_Iterable[str]] = ..., timeout_hours: _Optional[int] = ..., order: _Optional[int] = ...) -> None: ...
