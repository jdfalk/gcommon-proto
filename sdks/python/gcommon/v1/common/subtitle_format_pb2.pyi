from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SubtitleFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBTITLE_FORMAT_UNSPECIFIED: _ClassVar[SubtitleFormat]
    SUBTITLE_FORMAT_SRT: _ClassVar[SubtitleFormat]
    SUBTITLE_FORMAT_VTT: _ClassVar[SubtitleFormat]
    SUBTITLE_FORMAT_ASS: _ClassVar[SubtitleFormat]
    SUBTITLE_FORMAT_SSA: _ClassVar[SubtitleFormat]
    SUBTITLE_FORMAT_TTML: _ClassVar[SubtitleFormat]
    SUBTITLE_FORMAT_SCC: _ClassVar[SubtitleFormat]
    SUBTITLE_FORMAT_SBV: _ClassVar[SubtitleFormat]
SUBTITLE_FORMAT_UNSPECIFIED: SubtitleFormat
SUBTITLE_FORMAT_SRT: SubtitleFormat
SUBTITLE_FORMAT_VTT: SubtitleFormat
SUBTITLE_FORMAT_ASS: SubtitleFormat
SUBTITLE_FORMAT_SSA: SubtitleFormat
SUBTITLE_FORMAT_TTML: SubtitleFormat
SUBTITLE_FORMAT_SCC: SubtitleFormat
SUBTITLE_FORMAT_SBV: SubtitleFormat
