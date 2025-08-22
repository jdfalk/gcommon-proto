from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import metric_metadata_pb2 as _metric_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateMetricResponse(_message.Message):
    __slots__ = ("metadata", "error")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    metadata: _metric_metadata_pb2.MetricMetadata
    error: _error_pb2.Error
    def __init__(self, metadata: _Optional[_Union[_metric_metadata_pb2.MetricMetadata, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
