from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import metric_metadata_pb2 as _metric_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMetricMetadataRequest(_message.Message):
    __slots__ = ("metadata", "request_meta")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REQUEST_META_FIELD_NUMBER: _ClassVar[int]
    metadata: _metric_metadata_pb2.MetricMetadata
    request_meta: _request_metadata_pb2.RequestMetadata
    def __init__(
        self,
        metadata: _Optional[
            _Union[_metric_metadata_pb2.MetricMetadata, _Mapping]
        ] = ...,
        request_meta: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
    ) -> None: ...
