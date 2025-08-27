import datetime

from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Team(_message.Message):
    __slots__ = ("id", "organization_id", "department_id", "name", "slug", "description", "lead_id", "team_type", "focus_area", "metadata", "created_at", "updated_at", "created_by", "updated_by", "active", "contact_email", "communication_channel", "max_members", "budget_allocation", "timezone", "member_ids", "project_ids", "objectives", "kpis", "cross_functional")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LEAD_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    FOCUS_AREA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_ALLOCATION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    KPIS_FIELD_NUMBER: _ClassVar[int]
    CROSS_FUNCTIONAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    department_id: str
    name: str
    slug: str
    description: str
    lead_id: str
    team_type: str
    focus_area: str
    metadata: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: str
    updated_by: str
    active: bool
    contact_email: str
    communication_channel: str
    max_members: int
    budget_allocation: float
    timezone: str
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    project_ids: _containers.RepeatedScalarFieldContainer[str]
    objectives: _containers.RepeatedScalarFieldContainer[str]
    kpis: _containers.RepeatedScalarFieldContainer[str]
    cross_functional: bool
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., department_id: _Optional[str] = ..., name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., lead_id: _Optional[str] = ..., team_type: _Optional[str] = ..., focus_area: _Optional[str] = ..., metadata: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., updated_by: _Optional[str] = ..., active: _Optional[bool] = ..., contact_email: _Optional[str] = ..., communication_channel: _Optional[str] = ..., max_members: _Optional[int] = ..., budget_allocation: _Optional[float] = ..., timezone: _Optional[str] = ..., member_ids: _Optional[_Iterable[str]] = ..., project_ids: _Optional[_Iterable[str]] = ..., objectives: _Optional[_Iterable[str]] = ..., kpis: _Optional[_Iterable[str]] = ..., cross_functional: _Optional[bool] = ...) -> None: ...
