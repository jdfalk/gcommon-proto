from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AggregationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGGREGATION_TYPE_UNSPECIFIED: _ClassVar[AggregationType]
    AGGREGATION_TYPE_SUM: _ClassVar[AggregationType]
    AGGREGATION_TYPE_AVERAGE: _ClassVar[AggregationType]
    AGGREGATION_TYPE_MIN: _ClassVar[AggregationType]
    AGGREGATION_TYPE_MAX: _ClassVar[AggregationType]
    AGGREGATION_TYPE_COUNT: _ClassVar[AggregationType]
    AGGREGATION_TYPE_STDDEV: _ClassVar[AggregationType]
    AGGREGATION_TYPE_VARIANCE: _ClassVar[AggregationType]
    AGGREGATION_TYPE_MEDIAN: _ClassVar[AggregationType]
    AGGREGATION_TYPE_P95: _ClassVar[AggregationType]
    AGGREGATION_TYPE_P99: _ClassVar[AggregationType]
    AGGREGATION_TYPE_RATE: _ClassVar[AggregationType]
    AGGREGATION_TYPE_INCREASE: _ClassVar[AggregationType]
AGGREGATION_TYPE_UNSPECIFIED: AggregationType
AGGREGATION_TYPE_SUM: AggregationType
AGGREGATION_TYPE_AVERAGE: AggregationType
AGGREGATION_TYPE_MIN: AggregationType
AGGREGATION_TYPE_MAX: AggregationType
AGGREGATION_TYPE_COUNT: AggregationType
AGGREGATION_TYPE_STDDEV: AggregationType
AGGREGATION_TYPE_VARIANCE: AggregationType
AGGREGATION_TYPE_MEDIAN: AggregationType
AGGREGATION_TYPE_P95: AggregationType
AGGREGATION_TYPE_P99: AggregationType
AGGREGATION_TYPE_RATE: AggregationType
AGGREGATION_TYPE_INCREASE: AggregationType
