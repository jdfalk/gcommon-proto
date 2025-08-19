from gcommon.v1.web.messages import mime_type_pb2 as _mime_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileMetadata(_message.Message):
    __slots__ = ("name", "size_bytes", "mime_type", "checksum", "modified_at")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    size_bytes: int
    mime_type: _mime_type_pb2.MimeType
    checksum: str
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., size_bytes: _Optional[int] = ..., mime_type: _Optional[_Union[_mime_type_pb2.MimeType, _Mapping]] = ..., checksum: _Optional[str] = ..., modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
