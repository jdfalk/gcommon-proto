from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SampleRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAMPLE_RATE_UNSPECIFIED: _ClassVar[SampleRate]
    SAMPLE_RATE_FULL: _ClassVar[SampleRate]
    SAMPLE_RATE_HALF: _ClassVar[SampleRate]
    SAMPLE_RATE_QUARTER: _ClassVar[SampleRate]
    SAMPLE_RATE_TENTH: _ClassVar[SampleRate]
    SAMPLE_RATE_TWENTIETH: _ClassVar[SampleRate]
    SAMPLE_RATE_HUNDREDTH: _ClassVar[SampleRate]
    SAMPLE_RATE_THOUSANDTH: _ClassVar[SampleRate]
    SAMPLE_RATE_ADAPTIVE: _ClassVar[SampleRate]
    SAMPLE_RATE_CUSTOM: _ClassVar[SampleRate]
SAMPLE_RATE_UNSPECIFIED: SampleRate
SAMPLE_RATE_FULL: SampleRate
SAMPLE_RATE_HALF: SampleRate
SAMPLE_RATE_QUARTER: SampleRate
SAMPLE_RATE_TENTH: SampleRate
SAMPLE_RATE_TWENTIETH: SampleRate
SAMPLE_RATE_HUNDREDTH: SampleRate
SAMPLE_RATE_THOUSANDTH: SampleRate
SAMPLE_RATE_ADAPTIVE: SampleRate
SAMPLE_RATE_CUSTOM: SampleRate
