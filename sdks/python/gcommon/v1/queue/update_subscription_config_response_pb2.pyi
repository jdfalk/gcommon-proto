from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSubscriptionConfigResponse(_message.Message):
    __slots__ = ("success", "subscription_id", "applied_changes", "warnings", "error")
    class AppliedChangesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    subscription_id: str
    applied_changes: _containers.ScalarMap[str, str]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    error: str
    def __init__(self, success: bool = ..., subscription_id: _Optional[str] = ..., applied_changes: _Optional[_Mapping[str, str]] = ..., warnings: _Optional[_Iterable[str]] = ..., error: _Optional[str] = ...) -> None: ...
