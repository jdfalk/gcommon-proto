from gcommon.v1.common import ordering_level_pb2 as _ordering_level_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderingConfig(_message.Message):
    __slots__ = (
        "global_ordering",
        "partition_ordering",
        "producer_ordering",
        "causal_ordering",
        "ordering_timeout_ms",
    )
    GLOBAL_ORDERING_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ORDERING_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_ORDERING_FIELD_NUMBER: _ClassVar[int]
    CAUSAL_ORDERING_FIELD_NUMBER: _ClassVar[int]
    ORDERING_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    global_ordering: _ordering_level_pb2.OrderingLevel
    partition_ordering: _ordering_level_pb2.OrderingLevel
    producer_ordering: _ordering_level_pb2.OrderingLevel
    causal_ordering: bool
    ordering_timeout_ms: int
    def __init__(
        self,
        global_ordering: _Optional[
            _Union[_ordering_level_pb2.OrderingLevel, str]
        ] = ...,
        partition_ordering: _Optional[
            _Union[_ordering_level_pb2.OrderingLevel, str]
        ] = ...,
        producer_ordering: _Optional[
            _Union[_ordering_level_pb2.OrderingLevel, str]
        ] = ...,
        causal_ordering: _Optional[bool] = ...,
        ordering_timeout_ms: _Optional[int] = ...,
    ) -> None: ...
