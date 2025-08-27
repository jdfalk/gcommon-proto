from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StatisticType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATISTIC_TYPE_UNSPECIFIED: _ClassVar[StatisticType]
    STATISTIC_TYPE_MESSAGE_COUNT: _ClassVar[StatisticType]
    STATISTIC_TYPE_THROUGHPUT: _ClassVar[StatisticType]
    STATISTIC_TYPE_LATENCY: _ClassVar[StatisticType]
    STATISTIC_TYPE_ERROR_RATE: _ClassVar[StatisticType]
    STATISTIC_TYPE_QUEUE_DEPTH: _ClassVar[StatisticType]
    STATISTIC_TYPE_PROCESSING_TIME: _ClassVar[StatisticType]
    STATISTIC_TYPE_CONSUMER_COUNT: _ClassVar[StatisticType]
    STATISTIC_TYPE_MESSAGE_SIZE: _ClassVar[StatisticType]
    STATISTIC_TYPE_AGE_DISTRIBUTION: _ClassVar[StatisticType]
    STATISTIC_TYPE_SUCCESS_RATE: _ClassVar[StatisticType]

STATISTIC_TYPE_UNSPECIFIED: StatisticType
STATISTIC_TYPE_MESSAGE_COUNT: StatisticType
STATISTIC_TYPE_THROUGHPUT: StatisticType
STATISTIC_TYPE_LATENCY: StatisticType
STATISTIC_TYPE_ERROR_RATE: StatisticType
STATISTIC_TYPE_QUEUE_DEPTH: StatisticType
STATISTIC_TYPE_PROCESSING_TIME: StatisticType
STATISTIC_TYPE_CONSUMER_COUNT: StatisticType
STATISTIC_TYPE_MESSAGE_SIZE: StatisticType
STATISTIC_TYPE_AGE_DISTRIBUTION: StatisticType
STATISTIC_TYPE_SUCCESS_RATE: StatisticType
