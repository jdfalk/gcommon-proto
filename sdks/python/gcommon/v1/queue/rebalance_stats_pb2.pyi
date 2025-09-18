import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RebalanceStats(_message.Message):
    __slots__ = ("total_rebalances", "last_rebalance", "avg_rebalance_duration_ms", "failed_rebalances")
    TOTAL_REBALANCES_FIELD_NUMBER: _ClassVar[int]
    LAST_REBALANCE_FIELD_NUMBER: _ClassVar[int]
    AVG_REBALANCE_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    FAILED_REBALANCES_FIELD_NUMBER: _ClassVar[int]
    total_rebalances: int
    last_rebalance: _timestamp_pb2.Timestamp
    avg_rebalance_duration_ms: int
    failed_rebalances: int
    def __init__(self, total_rebalances: _Optional[int] = ..., last_rebalance: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., avg_rebalance_duration_ms: _Optional[int] = ..., failed_rebalances: _Optional[int] = ...) -> None: ...
