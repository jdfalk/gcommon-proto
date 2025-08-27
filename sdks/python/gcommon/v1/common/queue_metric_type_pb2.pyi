from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QueueMetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUEUE_METRIC_TYPE_UNSPECIFIED: _ClassVar[QueueMetricType]
    QUEUE_METRIC_TYPE_MESSAGE_COUNT: _ClassVar[QueueMetricType]
    QUEUE_METRIC_TYPE_MESSAGE_RATE: _ClassVar[QueueMetricType]
    QUEUE_METRIC_TYPE_PROCESSING_TIME: _ClassVar[QueueMetricType]
    QUEUE_METRIC_TYPE_ERROR_RATE: _ClassVar[QueueMetricType]
    QUEUE_METRIC_TYPE_CONSUMER_COUNT: _ClassVar[QueueMetricType]
    QUEUE_METRIC_TYPE_QUEUE_DEPTH: _ClassVar[QueueMetricType]

QUEUE_METRIC_TYPE_UNSPECIFIED: QueueMetricType
QUEUE_METRIC_TYPE_MESSAGE_COUNT: QueueMetricType
QUEUE_METRIC_TYPE_MESSAGE_RATE: QueueMetricType
QUEUE_METRIC_TYPE_PROCESSING_TIME: QueueMetricType
QUEUE_METRIC_TYPE_ERROR_RATE: QueueMetricType
QUEUE_METRIC_TYPE_CONSUMER_COUNT: QueueMetricType
QUEUE_METRIC_TYPE_QUEUE_DEPTH: QueueMetricType
