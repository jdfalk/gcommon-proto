from gcommon.v1.metrics.messages import time_range_pb2 as _time_range_pb2
from gcommon.v1.queue.enums import export_format_pb2 as _export_format_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportQueueRequest(_message.Message):
    __slots__ = ("queue_name", "destination", "format", "include_message_data", "time_range", "compress", "max_messages", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MESSAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    COMPRESS_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    destination: str
    format: _export_format_pb2.QueueExportFormat
    include_message_data: bool
    time_range: _time_range_pb2.MetricsTimeRange
    compress: bool
    max_messages: int
    options: _containers.ScalarMap[str, str]
    def __init__(self, queue_name: _Optional[str] = ..., destination: _Optional[str] = ..., format: _Optional[_Union[_export_format_pb2.QueueExportFormat, str]] = ..., include_message_data: bool = ..., time_range: _Optional[_Union[_time_range_pb2.MetricsTimeRange, _Mapping]] = ..., compress: bool = ..., max_messages: _Optional[int] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...
