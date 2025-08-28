from gcommon.v1.common import stream_compression_pb2 as _stream_compression_pb2
from gcommon.v1.common import stream_qos_pb2 as _stream_qos_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamOptions(_message.Message):
    __slots__ = ("include_historical", "batch_size", "batch_timeout_ms", "include_metadata", "compression", "send_heartbeats", "heartbeat_interval_seconds", "auto_retry", "qos")
    INCLUDE_HISTORICAL_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    BATCH_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    SEND_HEARTBEATS_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AUTO_RETRY_FIELD_NUMBER: _ClassVar[int]
    QOS_FIELD_NUMBER: _ClassVar[int]
    include_historical: bool
    batch_size: int
    batch_timeout_ms: int
    include_metadata: bool
    compression: _stream_compression_pb2.StreamCompression
    send_heartbeats: bool
    heartbeat_interval_seconds: int
    auto_retry: bool
    qos: _stream_qos_pb2.StreamQOS
    def __init__(self, include_historical: bool = ..., batch_size: _Optional[int] = ..., batch_timeout_ms: _Optional[int] = ..., include_metadata: bool = ..., compression: _Optional[_Union[_stream_compression_pb2.StreamCompression, str]] = ..., send_heartbeats: bool = ..., heartbeat_interval_seconds: _Optional[int] = ..., auto_retry: bool = ..., qos: _Optional[_Union[_stream_qos_pb2.StreamQOS, str]] = ...) -> None: ...
