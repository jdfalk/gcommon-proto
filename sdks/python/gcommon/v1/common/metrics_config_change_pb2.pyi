from gcommon.v1.common import change_type_pb2 as _change_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsConfigChange(_message.Message):
    __slots__ = ("change_type", "setting_path", "old_value", "new_value", "description")
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SETTING_PATH_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    change_type: _change_type_pb2.MetricsChangeType
    setting_path: str
    old_value: str
    new_value: str
    description: str
    def __init__(self, change_type: _Optional[_Union[_change_type_pb2.MetricsChangeType, str]] = ..., setting_path: _Optional[str] = ..., old_value: _Optional[str] = ..., new_value: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
