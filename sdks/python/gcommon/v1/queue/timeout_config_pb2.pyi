import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueTimeoutConfig(_message.Message):
    __slots__ = (
        "publish_timeout",
        "consume_timeout",
        "ack_timeout",
        "connect_timeout",
        "processing_timeout",
        "management_timeout",
        "health_check_timeout",
        "subscription_timeout",
    )
    PUBLISH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CONSUME_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ACK_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CONNECT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    publish_timeout: _duration_pb2.Duration
    consume_timeout: _duration_pb2.Duration
    ack_timeout: _duration_pb2.Duration
    connect_timeout: _duration_pb2.Duration
    processing_timeout: _duration_pb2.Duration
    management_timeout: _duration_pb2.Duration
    health_check_timeout: _duration_pb2.Duration
    subscription_timeout: _duration_pb2.Duration
    def __init__(
        self,
        publish_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        consume_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        ack_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        connect_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        processing_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        management_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        health_check_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        subscription_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
    ) -> None: ...
