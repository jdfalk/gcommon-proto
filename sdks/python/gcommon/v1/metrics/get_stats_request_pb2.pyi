from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import timestamp_range_pb2 as _timestamp_range_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsGetStatsRequest(_message.Message):
    __slots__ = ("metric", "range", "metadata")
    METRIC_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metric: str
    range: _timestamp_range_pb2.MetricsTimestampRange
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(
        self,
        metric: _Optional[str] = ...,
        range: _Optional[
            _Union[_timestamp_range_pb2.MetricsTimestampRange, _Mapping]
        ] = ...,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
    ) -> None: ...
