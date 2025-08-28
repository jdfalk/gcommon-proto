from gcommon.v1.common import pagination_pb2 as _pagination_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeysRequest(_message.Message):
    __slots__ = ("pattern", "namespace", "pagination", "metadata")
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    namespace: str
    pagination: _pagination_pb2.Pagination
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, pattern: _Optional[str] = ..., namespace: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.Pagination, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
