from gcommon.v1.common import audit_result_pb2 as _audit_result_pb2
from gcommon.v1.common import resource_reference_pb2 as _resource_reference_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonAuditLog(_message.Message):
    __slots__ = ("id", "user_id", "action", "resource", "timestamp", "source_ip", "user_agent", "metadata", "result", "session_id")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    action: str
    resource: _resource_reference_pb2.ResourceReference
    timestamp: _timestamp_pb2.Timestamp
    source_ip: str
    user_agent: str
    metadata: _containers.ScalarMap[str, str]
    result: _audit_result_pb2.AuditResult
    session_id: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., action: _Optional[str] = ..., resource: _Optional[_Union[_resource_reference_pb2.ResourceReference, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source_ip: _Optional[str] = ..., user_agent: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., result: _Optional[_Union[_audit_result_pb2.AuditResult, str]] = ..., session_id: _Optional[str] = ...) -> None: ...
