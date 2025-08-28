from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueRetentionInfo(_message.Message):
    __slots__ = ("retention_policy", "retention_seconds", "retention_bytes", "retained_messages", "oldest_message_time", "next_cleanup_time")
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    RETENTION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_BYTES_FIELD_NUMBER: _ClassVar[int]
    RETAINED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    OLDEST_MESSAGE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_CLEANUP_TIME_FIELD_NUMBER: _ClassVar[int]
    retention_policy: str
    retention_seconds: int
    retention_bytes: int
    retained_messages: int
    oldest_message_time: _timestamp_pb2.Timestamp
    next_cleanup_time: _timestamp_pb2.Timestamp
    def __init__(self, retention_policy: _Optional[str] = ..., retention_seconds: _Optional[int] = ..., retention_bytes: _Optional[int] = ..., retained_messages: _Optional[int] = ..., oldest_message_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_cleanup_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
