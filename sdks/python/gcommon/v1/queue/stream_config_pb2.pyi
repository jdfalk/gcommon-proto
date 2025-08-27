import datetime

from gcommon.v1.common import stream_restart_policy_pb2 as _stream_restart_policy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamConfig(_message.Message):
    __slots__ = (
        "buffer_size",
        "read_timeout",
        "flow_control_enabled",
        "max_outstanding_messages",
        "max_outstanding_bytes",
        "auto_ack",
        "ack_deadline",
        "enable_message_ordering",
        "restart_policy",
    )
    BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    READ_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    FLOW_CONTROL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTSTANDING_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTSTANDING_BYTES_FIELD_NUMBER: _ClassVar[int]
    AUTO_ACK_FIELD_NUMBER: _ClassVar[int]
    ACK_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MESSAGE_ORDERING_FIELD_NUMBER: _ClassVar[int]
    RESTART_POLICY_FIELD_NUMBER: _ClassVar[int]
    buffer_size: int
    read_timeout: _duration_pb2.Duration
    flow_control_enabled: bool
    max_outstanding_messages: int
    max_outstanding_bytes: int
    auto_ack: bool
    ack_deadline: _duration_pb2.Duration
    enable_message_ordering: bool
    restart_policy: _stream_restart_policy_pb2.StreamRestartPolicy
    def __init__(
        self,
        buffer_size: _Optional[int] = ...,
        read_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        flow_control_enabled: _Optional[bool] = ...,
        max_outstanding_messages: _Optional[int] = ...,
        max_outstanding_bytes: _Optional[int] = ...,
        auto_ack: _Optional[bool] = ...,
        ack_deadline: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        enable_message_ordering: _Optional[bool] = ...,
        restart_policy: _Optional[
            _Union[_stream_restart_policy_pb2.StreamRestartPolicy, str]
        ] = ...,
    ) -> None: ...
