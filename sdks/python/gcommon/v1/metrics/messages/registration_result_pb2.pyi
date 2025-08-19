from gcommon.v1.metrics.enums import registration_action_pb2 as _registration_action_pb2
from gcommon.v1.metrics.messages import schema_change_pb2 as _schema_change_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegistrationResult(_message.Message):
    __slots__ = ("action", "created_indices", "created_alerts", "configured_exports", "applied_retention_policies", "schema_changes")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_INDICES_FIELD_NUMBER: _ClassVar[int]
    CREATED_ALERTS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_RETENTION_POLICIES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_CHANGES_FIELD_NUMBER: _ClassVar[int]
    action: _registration_action_pb2.RegistrationAction
    created_indices: _containers.RepeatedScalarFieldContainer[str]
    created_alerts: _containers.RepeatedScalarFieldContainer[str]
    configured_exports: _containers.RepeatedScalarFieldContainer[str]
    applied_retention_policies: _containers.RepeatedScalarFieldContainer[str]
    schema_changes: _containers.RepeatedCompositeFieldContainer[_schema_change_pb2.SchemaChange]
    def __init__(self, action: _Optional[_Union[_registration_action_pb2.RegistrationAction, str]] = ..., created_indices: _Optional[_Iterable[str]] = ..., created_alerts: _Optional[_Iterable[str]] = ..., configured_exports: _Optional[_Iterable[str]] = ..., applied_retention_policies: _Optional[_Iterable[str]] = ..., schema_changes: _Optional[_Iterable[_Union[_schema_change_pb2.SchemaChange, _Mapping]]] = ...) -> None: ...
