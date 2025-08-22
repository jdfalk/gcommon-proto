from gcommon.v1.config import compliance_audit_pb2 as _compliance_audit_pb2
from gcommon.v1.config import compliance_reporting_pb2 as _compliance_reporting_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigComplianceSettings(_message.Message):
    __slots__ = ("frameworks", "policies", "audits", "reporting", "validation_enabled", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FRAMEWORKS_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    AUDITS_FIELD_NUMBER: _ClassVar[int]
    REPORTING_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    frameworks: _containers.RepeatedScalarFieldContainer[str]
    policies: _containers.RepeatedScalarFieldContainer[str]
    audits: _containers.RepeatedCompositeFieldContainer[_compliance_audit_pb2.ComplianceAudit]
    reporting: _compliance_reporting_pb2.ComplianceReporting
    validation_enabled: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, frameworks: _Optional[_Iterable[str]] = ..., policies: _Optional[_Iterable[str]] = ..., audits: _Optional[_Iterable[_Union[_compliance_audit_pb2.ComplianceAudit, _Mapping]]] = ..., reporting: _Optional[_Union[_compliance_reporting_pb2.ComplianceReporting, _Mapping]] = ..., validation_enabled: bool = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
