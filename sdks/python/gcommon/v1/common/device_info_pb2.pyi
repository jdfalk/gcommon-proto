from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceInfo(_message.Message):
    __slots__ = ("device_id", "device_type", "os", "browser", "is_trusted")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    BROWSER_FIELD_NUMBER: _ClassVar[int]
    IS_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    device_type: str
    os: str
    browser: str
    is_trusted: bool
    def __init__(self, device_id: _Optional[str] = ..., device_type: _Optional[str] = ..., os: _Optional[str] = ..., browser: _Optional[str] = ..., is_trusted: _Optional[bool] = ...) -> None: ...
