from gcommon.v1.organization import storage_backup_config_pb2 as _storage_backup_config_pb2
from gcommon.v1.organization import storage_encryption_pb2 as _storage_encryption_pb2
from gcommon.v1.organization import storage_policy_pb2 as _storage_policy_pb2
from gcommon.v1.organization import storage_quota_pb2 as _storage_quota_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorageIsolation(_message.Message):
    __slots__ = ("storage_bucket", "path_prefix", "dedicated_storage", "encryption", "policies", "backup", "quota")
    STORAGE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_STORAGE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    storage_bucket: str
    path_prefix: str
    dedicated_storage: bool
    encryption: _storage_encryption_pb2.StorageEncryption
    policies: _containers.RepeatedCompositeFieldContainer[_storage_policy_pb2.StoragePolicy]
    backup: _storage_backup_config_pb2.StorageBackupConfig
    quota: _storage_quota_pb2.StorageQuota
    def __init__(self, storage_bucket: _Optional[str] = ..., path_prefix: _Optional[str] = ..., dedicated_storage: bool = ..., encryption: _Optional[_Union[_storage_encryption_pb2.StorageEncryption, _Mapping]] = ..., policies: _Optional[_Iterable[_Union[_storage_policy_pb2.StoragePolicy, _Mapping]]] = ..., backup: _Optional[_Union[_storage_backup_config_pb2.StorageBackupConfig, _Mapping]] = ..., quota: _Optional[_Union[_storage_quota_pb2.StorageQuota, _Mapping]] = ...) -> None: ...
