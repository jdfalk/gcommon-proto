import datetime

from gcommon.v1.common import gauge_operation_pb2 as _gauge_operation_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordGaugeRequest(_message.Message):
    __slots__ = (
        "name",
        "value",
        "labels",
        "help",
        "unit",
        "timestamp",
        "metadata",
        "operation",
    )
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: float
    labels: _containers.ScalarMap[str, str]
    help: str
    unit: str
    timestamp: _timestamp_pb2.Timestamp
    metadata: _request_metadata_pb2.RequestMetadata
    operation: _gauge_operation_pb2.GaugeOperation
    def __init__(
        self,
        name: _Optional[str] = ...,
        value: _Optional[float] = ...,
        labels: _Optional[_Mapping[str, str]] = ...,
        help: _Optional[str] = ...,
        unit: _Optional[str] = ...,
        timestamp: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
        operation: _Optional[_Union[_gauge_operation_pb2.GaugeOperation, str]] = ...,
    ) -> None: ...
