from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.media import silent_segment_pb2 as _silent_segment_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AudioAnalysis(_message.Message):
    __slots__ = ("peak_level", "rms_level", "silent_segments", "dynamic_range")
    PEAK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RMS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SILENT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_RANGE_FIELD_NUMBER: _ClassVar[int]
    peak_level: float
    rms_level: float
    silent_segments: _containers.RepeatedCompositeFieldContainer[_silent_segment_pb2.SilentSegment]
    dynamic_range: float
    def __init__(self, peak_level: _Optional[float] = ..., rms_level: _Optional[float] = ..., silent_segments: _Optional[_Iterable[_Union[_silent_segment_pb2.SilentSegment, _Mapping]]] = ..., dynamic_range: _Optional[float] = ...) -> None: ...
