from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BackupFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKUP_FREQUENCY_UNSPECIFIED: _ClassVar[BackupFrequency]
    BACKUP_FREQUENCY_MANUAL: _ClassVar[BackupFrequency]
    BACKUP_FREQUENCY_HOURLY: _ClassVar[BackupFrequency]
    BACKUP_FREQUENCY_DAILY: _ClassVar[BackupFrequency]
    BACKUP_FREQUENCY_WEEKLY: _ClassVar[BackupFrequency]
    BACKUP_FREQUENCY_MONTHLY: _ClassVar[BackupFrequency]
    BACKUP_FREQUENCY_ON_CHANGE: _ClassVar[BackupFrequency]
BACKUP_FREQUENCY_UNSPECIFIED: BackupFrequency
BACKUP_FREQUENCY_MANUAL: BackupFrequency
BACKUP_FREQUENCY_HOURLY: BackupFrequency
BACKUP_FREQUENCY_DAILY: BackupFrequency
BACKUP_FREQUENCY_WEEKLY: BackupFrequency
BACKUP_FREQUENCY_MONTHLY: BackupFrequency
BACKUP_FREQUENCY_ON_CHANGE: BackupFrequency
