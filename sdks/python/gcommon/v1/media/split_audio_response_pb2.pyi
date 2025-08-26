from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SplitAudioResponse(_message.Message):
    __slots__ = ("segment_file_ids",)
    SEGMENT_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    segment_file_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, segment_file_ids: _Optional[_Iterable[str]] = ...) -> None: ...
