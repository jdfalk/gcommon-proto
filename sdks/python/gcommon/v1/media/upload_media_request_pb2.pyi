from gcommon.v1.media import media_metadata_pb2 as _media_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadMediaRequest(_message.Message):
    __slots__ = ("metadata", "chunk")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    metadata: UploadMetadata
    chunk: bytes
    def __init__(self, metadata: _Optional[_Union[UploadMetadata, _Mapping]] = ..., chunk: _Optional[bytes] = ...) -> None: ...

class UploadMetadata(_message.Message):
    __slots__ = ("filename", "content_type", "total_size", "media_metadata")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_METADATA_FIELD_NUMBER: _ClassVar[int]
    filename: str
    content_type: str
    total_size: int
    media_metadata: _media_metadata_pb2.MediaMetadata
    def __init__(self, filename: _Optional[str] = ..., content_type: _Optional[str] = ..., total_size: _Optional[int] = ..., media_metadata: _Optional[_Union[_media_metadata_pb2.MediaMetadata, _Mapping]] = ...) -> None: ...
