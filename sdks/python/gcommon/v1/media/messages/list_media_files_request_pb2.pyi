from gcommon.v1.media.enums import media_type_pb2 as _media_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMediaFilesRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "media_type", "path_prefix", "include_metadata")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    media_type: _media_type_pb2.MediaType
    path_prefix: str
    include_metadata: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., media_type: _Optional[_Union[_media_type_pb2.MediaType, str]] = ..., path_prefix: _Optional[str] = ..., include_metadata: bool = ...) -> None: ...
