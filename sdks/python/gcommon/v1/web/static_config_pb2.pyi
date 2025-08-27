from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StaticConfig(_message.Message):
    __slots__ = ("directory", "index_files", "enable_listing")
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    INDEX_FILES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LISTING_FIELD_NUMBER: _ClassVar[int]
    directory: str
    index_files: _containers.RepeatedScalarFieldContainer[str]
    enable_listing: bool
    def __init__(
        self,
        directory: _Optional[str] = ...,
        index_files: _Optional[_Iterable[str]] = ...,
        enable_listing: _Optional[bool] = ...,
    ) -> None: ...
