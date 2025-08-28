from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreWarning(_message.Message):
    __slots__ = ("warning_code", "warning_message", "warning_category", "affected_component", "partition_id", "warning_time")
    WARNING_CODE_FIELD_NUMBER: _ClassVar[int]
    WARNING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    WARNING_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    WARNING_TIME_FIELD_NUMBER: _ClassVar[int]
    warning_code: str
    warning_message: str
    warning_category: str
    affected_component: str
    partition_id: int
    warning_time: _timestamp_pb2.Timestamp
    def __init__(self, warning_code: _Optional[str] = ..., warning_message: _Optional[str] = ..., warning_category: _Optional[str] = ..., affected_component: _Optional[str] = ..., partition_id: _Optional[int] = ..., warning_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
