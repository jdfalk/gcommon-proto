from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTenantsRequest(_message.Message):
    __slots__ = ("metadata", "organization_id", "page_size", "page_token", "filter")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    organization_id: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., organization_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...
