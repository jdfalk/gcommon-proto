from gcommon.v1.common import rollback_method_pb2 as _rollback_method_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RollbackInfo(_message.Message):
    __slots__ = ("original_audit_id", "reason", "method", "target_version", "automatic")
    ORIGINAL_AUDIT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    original_audit_id: str
    reason: str
    method: _rollback_method_pb2.RollbackMethod
    target_version: str
    automatic: bool
    def __init__(self, original_audit_id: _Optional[str] = ..., reason: _Optional[str] = ..., method: _Optional[_Union[_rollback_method_pb2.RollbackMethod, str]] = ..., target_version: _Optional[str] = ..., automatic: _Optional[bool] = ...) -> None: ...
