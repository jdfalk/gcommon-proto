from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SplitAudioResponse(_message.Message):
    __slots__ = ("segment_file_ids",)
    SEGMENT_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    segment_file_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, segment_file_ids: _Optional[_Iterable[str]] = ...) -> None: ...
