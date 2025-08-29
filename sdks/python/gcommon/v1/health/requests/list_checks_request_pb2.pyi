from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListChecksRequest(_message.Message):
    __slots__ = ("service_name", "check_type", "tags", "metadata", "enabled_only", "limit", "offset")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    CHECK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ENABLED_ONLY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    check_type: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    metadata: _request_metadata_pb2.RequestMetadata
    enabled_only: bool
    limit: int
    offset: int
    def __init__(self, service_name: _Optional[str] = ..., check_type: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., enabled_only: bool = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...
