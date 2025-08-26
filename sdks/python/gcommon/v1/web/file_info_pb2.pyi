import datetime

from gcommon.v1.web import mime_type_pb2 as _mime_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileInfo(_message.Message):
    __slots__ = ("path", "size_bytes", "mime_type", "modified_at", "checksum")
    PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    path: str
    size_bytes: int
    mime_type: _mime_type_pb2.MimeType
    modified_at: _timestamp_pb2.Timestamp
    checksum: str
    def __init__(self, path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., mime_type: _Optional[_Union[_mime_type_pb2.MimeType, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., checksum: _Optional[str] = ...) -> None: ...
