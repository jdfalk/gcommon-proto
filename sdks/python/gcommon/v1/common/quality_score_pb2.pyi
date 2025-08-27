from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QualityScore(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUALITY_SCORE_UNSPECIFIED: _ClassVar[QualityScore]
    QUALITY_SCORE_LOW: _ClassVar[QualityScore]
    QUALITY_SCORE_MEDIUM: _ClassVar[QualityScore]
    QUALITY_SCORE_HIGH: _ClassVar[QualityScore]
    QUALITY_SCORE_EXCELLENT: _ClassVar[QualityScore]

QUALITY_SCORE_UNSPECIFIED: QualityScore
QUALITY_SCORE_LOW: QualityScore
QUALITY_SCORE_MEDIUM: QualityScore
QUALITY_SCORE_HIGH: QualityScore
QUALITY_SCORE_EXCELLENT: QualityScore
