from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StatsGranularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATS_GRANULARITY_UNSPECIFIED: _ClassVar[StatsGranularity]
    STATS_GRANULARITY_MINUTE: _ClassVar[StatsGranularity]
    STATS_GRANULARITY_HOUR: _ClassVar[StatsGranularity]
    STATS_GRANULARITY_DAY: _ClassVar[StatsGranularity]
    STATS_GRANULARITY_WEEK: _ClassVar[StatsGranularity]
STATS_GRANULARITY_UNSPECIFIED: StatsGranularity
STATS_GRANULARITY_MINUTE: StatsGranularity
STATS_GRANULARITY_HOUR: StatsGranularity
STATS_GRANULARITY_DAY: StatsGranularity
STATS_GRANULARITY_WEEK: StatsGranularity
