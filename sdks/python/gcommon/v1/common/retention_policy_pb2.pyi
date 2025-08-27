from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsRetentionPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RETENTION_POLICY_UNSPECIFIED: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_SHORT_TERM: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_MEDIUM_TERM: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_LONG_TERM: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_ARCHIVE: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_CUSTOM: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_HIGH_FREQUENCY: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_LOW_FREQUENCY: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_COMPLIANCE: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_REAL_TIME: _ClassVar[MetricsRetentionPolicy]
    RETENTION_POLICY_AGGREGATE: _ClassVar[MetricsRetentionPolicy]

RETENTION_POLICY_UNSPECIFIED: MetricsRetentionPolicy
RETENTION_POLICY_SHORT_TERM: MetricsRetentionPolicy
RETENTION_POLICY_MEDIUM_TERM: MetricsRetentionPolicy
RETENTION_POLICY_LONG_TERM: MetricsRetentionPolicy
RETENTION_POLICY_ARCHIVE: MetricsRetentionPolicy
RETENTION_POLICY_CUSTOM: MetricsRetentionPolicy
RETENTION_POLICY_HIGH_FREQUENCY: MetricsRetentionPolicy
RETENTION_POLICY_LOW_FREQUENCY: MetricsRetentionPolicy
RETENTION_POLICY_COMPLIANCE: MetricsRetentionPolicy
RETENTION_POLICY_REAL_TIME: MetricsRetentionPolicy
RETENTION_POLICY_AGGREGATE: MetricsRetentionPolicy
