from gcommon.v1.web import mime_type_pb2 as _mime_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileUpload(_message.Message):
    __slots__ = ("file_name", "content_type", "data", "destination")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    content_type: _mime_type_pb2.MimeType
    data: bytes
    destination: str
    def __init__(self, file_name: _Optional[str] = ..., content_type: _Optional[_Union[_mime_type_pb2.MimeType, _Mapping]] = ..., data: _Optional[bytes] = ..., destination: _Optional[str] = ...) -> None: ...
