from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchHealthRequest(_message.Message):
    __slots__ = ("service_name", "check_id", "metadata", "status_changes_only", "tags")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_CHANGES_ONLY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    check_id: str
    metadata: _request_metadata_pb2.RequestMetadata
    status_changes_only: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, service_name: _Optional[str] = ..., check_id: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., status_changes_only: _Optional[bool] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
