import datetime

from gcommon.v1.queue import encryption_info_pb2 as _encryption_info_pb2
from gcommon.v1.queue import original_queue_info_pb2 as _original_queue_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupSource(_message.Message):
    __slots__ = ("backup_id", "backup_path", "storage_type", "credentials", "backup_timestamp", "original_queue", "backup_version", "compression_format", "encryption")
    class CredentialsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PATH_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_QUEUE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FORMAT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    backup_id: str
    backup_path: str
    storage_type: str
    credentials: _containers.ScalarMap[str, str]
    backup_timestamp: _timestamp_pb2.Timestamp
    original_queue: _original_queue_info_pb2.OriginalQueueInfo
    backup_version: str
    compression_format: str
    encryption: _encryption_info_pb2.EncryptionInfo
    def __init__(self, backup_id: _Optional[str] = ..., backup_path: _Optional[str] = ..., storage_type: _Optional[str] = ..., credentials: _Optional[_Mapping[str, str]] = ..., backup_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., original_queue: _Optional[_Union[_original_queue_info_pb2.OriginalQueueInfo, _Mapping]] = ..., backup_version: _Optional[str] = ..., compression_format: _Optional[str] = ..., encryption: _Optional[_Union[_encryption_info_pb2.EncryptionInfo, _Mapping]] = ...) -> None: ...
