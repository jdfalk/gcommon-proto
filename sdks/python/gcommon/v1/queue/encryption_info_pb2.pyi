from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EncryptionInfo(_message.Message):
    __slots__ = ("enabled", "algorithm", "kms_provider", "key_id")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    KMS_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    algorithm: str
    kms_provider: str
    key_id: str
    def __init__(self, enabled: _Optional[bool] = ..., algorithm: _Optional[str] = ..., kms_provider: _Optional[str] = ..., key_id: _Optional[str] = ...) -> None: ...
