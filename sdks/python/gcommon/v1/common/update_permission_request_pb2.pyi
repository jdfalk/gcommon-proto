from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdatePermissionRequest(_message.Message):
    __slots__ = ("permission_id", "name", "description", "resource", "action", "conditions", "active", "update_mask", "metadata", "reason")
    PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    permission_id: str
    name: str
    description: str
    resource: str
    action: str
    conditions: _containers.RepeatedScalarFieldContainer[str]
    active: bool
    update_mask: _containers.RepeatedScalarFieldContainer[str]
    metadata: _request_metadata_pb2.RequestMetadata
    reason: str
    def __init__(self, permission_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., resource: _Optional[str] = ..., action: _Optional[str] = ..., conditions: _Optional[_Iterable[str]] = ..., active: _Optional[bool] = ..., update_mask: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...
