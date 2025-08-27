from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SecretBackupFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECRET_BACKUP_FREQUENCY_UNSPECIFIED: _ClassVar[SecretBackupFrequency]
    SECRET_BACKUP_FREQUENCY_MANUAL: _ClassVar[SecretBackupFrequency]
    SECRET_BACKUP_FREQUENCY_HOURLY: _ClassVar[SecretBackupFrequency]
    SECRET_BACKUP_FREQUENCY_DAILY: _ClassVar[SecretBackupFrequency]
    SECRET_BACKUP_FREQUENCY_WEEKLY: _ClassVar[SecretBackupFrequency]
    SECRET_BACKUP_FREQUENCY_MONTHLY: _ClassVar[SecretBackupFrequency]
    SECRET_BACKUP_FREQUENCY_ON_CHANGE: _ClassVar[SecretBackupFrequency]
SECRET_BACKUP_FREQUENCY_UNSPECIFIED: SecretBackupFrequency
SECRET_BACKUP_FREQUENCY_MANUAL: SecretBackupFrequency
SECRET_BACKUP_FREQUENCY_HOURLY: SecretBackupFrequency
SECRET_BACKUP_FREQUENCY_DAILY: SecretBackupFrequency
SECRET_BACKUP_FREQUENCY_WEEKLY: SecretBackupFrequency
SECRET_BACKUP_FREQUENCY_MONTHLY: SecretBackupFrequency
SECRET_BACKUP_FREQUENCY_ON_CHANGE: SecretBackupFrequency
