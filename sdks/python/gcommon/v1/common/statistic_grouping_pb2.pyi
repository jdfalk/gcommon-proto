from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StatisticGrouping(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATISTIC_GROUPING_UNSPECIFIED: _ClassVar[StatisticGrouping]
    STATISTIC_GROUPING_NONE: _ClassVar[StatisticGrouping]
    STATISTIC_GROUPING_BY_QUEUE: _ClassVar[StatisticGrouping]
    STATISTIC_GROUPING_BY_CONSUMER: _ClassVar[StatisticGrouping]
    STATISTIC_GROUPING_BY_TIME_PERIOD: _ClassVar[StatisticGrouping]
    STATISTIC_GROUPING_BY_MESSAGE_TYPE: _ClassVar[StatisticGrouping]
STATISTIC_GROUPING_UNSPECIFIED: StatisticGrouping
STATISTIC_GROUPING_NONE: StatisticGrouping
STATISTIC_GROUPING_BY_QUEUE: StatisticGrouping
STATISTIC_GROUPING_BY_CONSUMER: StatisticGrouping
STATISTIC_GROUPING_BY_TIME_PERIOD: StatisticGrouping
STATISTIC_GROUPING_BY_MESSAGE_TYPE: StatisticGrouping
