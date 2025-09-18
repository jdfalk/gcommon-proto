from google.protobuf import go_features_pb2 as _go_features_pb2
from gcommon.v1.media import upload_metadata_pb2 as _upload_metadata_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadMediaRequest(_message.Message):
    __slots__ = ("metadata", "chunk")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    metadata: _upload_metadata_pb2.UploadMetadata
    chunk: bytes
    def __init__(self, metadata: _Optional[_Union[_upload_metadata_pb2.UploadMetadata, _Mapping]] = ..., chunk: _Optional[bytes] = ...) -> None: ...
