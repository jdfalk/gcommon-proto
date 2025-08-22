from gcommon.v1.queue import queue_info_pb2 as _queue_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetQueueInfoResponse(_message.Message):
    __slots__ = ("queue_info", "success", "error")
    QUEUE_INFO_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    queue_info: _queue_info_pb2.QueueInfo
    success: bool
    error: str
    def __init__(self, queue_info: _Optional[_Union[_queue_info_pb2.QueueInfo, _Mapping]] = ..., success: bool = ..., error: _Optional[str] = ...) -> None: ...
