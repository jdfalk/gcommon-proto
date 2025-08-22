from gcommon.v1.media import media_type_pb2 as _media_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchMediaRequest(_message.Message):
    __slots__ = ("query", "media_type", "tags", "language", "page_size", "page_token")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    query: str
    media_type: _media_type_pb2.MediaType
    tags: _containers.RepeatedScalarFieldContainer[str]
    language: str
    page_size: int
    page_token: str
    def __init__(self, query: _Optional[str] = ..., media_type: _Optional[_Union[_media_type_pb2.MediaType, str]] = ..., tags: _Optional[_Iterable[str]] = ..., language: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...
