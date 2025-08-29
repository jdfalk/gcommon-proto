from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.media import split_point_pb2 as _split_point_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SplitAudioRequest(_message.Message):
    __slots__ = ("audio_file_id", "split_points")
    AUDIO_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_POINTS_FIELD_NUMBER: _ClassVar[int]
    audio_file_id: str
    split_points: _containers.RepeatedCompositeFieldContainer[_split_point_pb2.SplitPoint]
    def __init__(self, audio_file_id: _Optional[str] = ..., split_points: _Optional[_Iterable[_Union[_split_point_pb2.SplitPoint, _Mapping]]] = ...) -> None: ...
