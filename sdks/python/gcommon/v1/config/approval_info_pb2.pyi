from gcommon.v1.config import approval_status_pb2 as _approval_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApprovalInfo(_message.Message):
    __slots__ = ("required", "status", "approved_by", "approved_at", "comments", "workflow_id", "policy_name")
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVED_BY_FIELD_NUMBER: _ClassVar[int]
    APPROVED_AT_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    required: bool
    status: _approval_status_pb2.ApprovalStatus
    approved_by: str
    approved_at: _timestamp_pb2.Timestamp
    comments: str
    workflow_id: str
    policy_name: str
    def __init__(self, required: bool = ..., status: _Optional[_Union[_approval_status_pb2.ApprovalStatus, str]] = ..., approved_by: _Optional[str] = ..., approved_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., comments: _Optional[str] = ..., workflow_id: _Optional[str] = ..., policy_name: _Optional[str] = ...) -> None: ...
