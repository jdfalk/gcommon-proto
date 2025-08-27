from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DashboardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DASHBOARD_TYPE_UNSPECIFIED: _ClassVar[DashboardType]
    DASHBOARD_TYPE_SYSTEM_OVERVIEW: _ClassVar[DashboardType]
    DASHBOARD_TYPE_APPLICATION_PERFORMANCE: _ClassVar[DashboardType]
    DASHBOARD_TYPE_INFRASTRUCTURE: _ClassVar[DashboardType]
    DASHBOARD_TYPE_BUSINESS_METRICS: _ClassVar[DashboardType]
    DASHBOARD_TYPE_SECURITY: _ClassVar[DashboardType]
    DASHBOARD_TYPE_CUSTOM: _ClassVar[DashboardType]
    DASHBOARD_TYPE_REAL_TIME: _ClassVar[DashboardType]
    DASHBOARD_TYPE_HISTORICAL: _ClassVar[DashboardType]
    DASHBOARD_TYPE_ALERT_SUMMARY: _ClassVar[DashboardType]
    DASHBOARD_TYPE_SERVICE_HEALTH: _ClassVar[DashboardType]
    DASHBOARD_TYPE_CAPACITY_PLANNING: _ClassVar[DashboardType]
    DASHBOARD_TYPE_SLA_SLO: _ClassVar[DashboardType]

DASHBOARD_TYPE_UNSPECIFIED: DashboardType
DASHBOARD_TYPE_SYSTEM_OVERVIEW: DashboardType
DASHBOARD_TYPE_APPLICATION_PERFORMANCE: DashboardType
DASHBOARD_TYPE_INFRASTRUCTURE: DashboardType
DASHBOARD_TYPE_BUSINESS_METRICS: DashboardType
DASHBOARD_TYPE_SECURITY: DashboardType
DASHBOARD_TYPE_CUSTOM: DashboardType
DASHBOARD_TYPE_REAL_TIME: DashboardType
DASHBOARD_TYPE_HISTORICAL: DashboardType
DASHBOARD_TYPE_ALERT_SUMMARY: DashboardType
DASHBOARD_TYPE_SERVICE_HEALTH: DashboardType
DASHBOARD_TYPE_CAPACITY_PLANNING: DashboardType
DASHBOARD_TYPE_SLA_SLO: DashboardType
