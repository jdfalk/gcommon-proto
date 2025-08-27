from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationComplianceSettings(_message.Message):
    __slots__ = (
        "gdpr_enabled",
        "data_retention_days",
        "data_export_enabled",
        "data_deletion_enabled",
        "certifications",
    )
    GDPR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATA_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    DATA_EXPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATA_DELETION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    gdpr_enabled: bool
    data_retention_days: int
    data_export_enabled: bool
    data_deletion_enabled: bool
    certifications: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        gdpr_enabled: _Optional[bool] = ...,
        data_retention_days: _Optional[int] = ...,
        data_export_enabled: _Optional[bool] = ...,
        data_deletion_enabled: _Optional[bool] = ...,
        certifications: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
