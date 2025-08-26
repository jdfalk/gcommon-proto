from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from gcommon.v1.web import file_info_pb2 as _file_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListFilesResponse(_message.Message):
    __slots__ = ("files", "total_count", "next_page_token", "has_more", "metadata")
    FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[_file_info_pb2.FileInfo]
    total_count: int
    next_page_token: str
    has_more: bool
    metadata: _response_metadata_pb2.ResponseMetadata
    def __init__(self, files: _Optional[_Iterable[_Union[_file_info_pb2.FileInfo, _Mapping]]] = ..., total_count: _Optional[int] = ..., next_page_token: _Optional[str] = ..., has_more: bool = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...
