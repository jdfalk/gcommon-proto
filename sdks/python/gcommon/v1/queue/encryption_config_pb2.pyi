from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueueEncryptionConfig(_message.Message):
    __slots__ = ("enabled", "algorithm", "key_derivation", "key_id", "encrypt_headers", "encrypt_routing_keys", "rotation_interval_hours")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    KEY_DERIVATION_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_ROUTING_KEYS_FIELD_NUMBER: _ClassVar[int]
    ROTATION_INTERVAL_HOURS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    algorithm: str
    key_derivation: str
    key_id: str
    encrypt_headers: bool
    encrypt_routing_keys: bool
    rotation_interval_hours: int
    def __init__(self, enabled: _Optional[bool] = ..., algorithm: _Optional[str] = ..., key_derivation: _Optional[str] = ..., key_id: _Optional[str] = ..., encrypt_headers: _Optional[bool] = ..., encrypt_routing_keys: _Optional[bool] = ..., rotation_interval_hours: _Optional[int] = ...) -> None: ...
