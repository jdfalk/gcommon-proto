from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContentUpdate(_message.Message):
    __slots__ = (
        "new_payload",
        "content_encoding",
        "content_type",
        "compression",
        "content_checksum",
    )
    NEW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    new_payload: _any_pb2.Any
    content_encoding: str
    content_type: str
    compression: str
    content_checksum: str
    def __init__(
        self,
        new_payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...,
        content_encoding: _Optional[str] = ...,
        content_type: _Optional[str] = ...,
        compression: _Optional[str] = ...,
        content_checksum: _Optional[str] = ...,
    ) -> None: ...
