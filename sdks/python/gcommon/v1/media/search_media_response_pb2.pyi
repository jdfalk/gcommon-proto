from gcommon.v1.media import media_file_pb2 as _media_file_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchMediaResponse(_message.Message):
    __slots__ = ("media_files", "next_page_token", "total_count", "suggested_terms")
    MEDIA_FILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_TERMS_FIELD_NUMBER: _ClassVar[int]
    media_files: _containers.RepeatedCompositeFieldContainer[_media_file_pb2.MediaFile]
    next_page_token: str
    total_count: int
    suggested_terms: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, media_files: _Optional[_Iterable[_Union[_media_file_pb2.MediaFile, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_count: _Optional[int] = ..., suggested_terms: _Optional[_Iterable[str]] = ...) -> None: ...
