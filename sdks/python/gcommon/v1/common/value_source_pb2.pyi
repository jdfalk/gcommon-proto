from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValueSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE_SOURCE_UNSPECIFIED: _ClassVar[ValueSource]
    VALUE_SOURCE_DEFAULT: _ClassVar[ValueSource]
    VALUE_SOURCE_ENVIRONMENT: _ClassVar[ValueSource]
    VALUE_SOURCE_FILE: _ClassVar[ValueSource]
    VALUE_SOURCE_DATABASE: _ClassVar[ValueSource]
    VALUE_SOURCE_CONSUL: _ClassVar[ValueSource]
    VALUE_SOURCE_ETCD: _ClassVar[ValueSource]
    VALUE_SOURCE_KUBERNETES: _ClassVar[ValueSource]
    VALUE_SOURCE_VAULT: _ClassVar[ValueSource]
    VALUE_SOURCE_AWS_PARAMETER_STORE: _ClassVar[ValueSource]
    VALUE_SOURCE_AWS_SECRETS_MANAGER: _ClassVar[ValueSource]
    VALUE_SOURCE_AZURE_KEY_VAULT: _ClassVar[ValueSource]
    VALUE_SOURCE_GCP_SECRET_MANAGER: _ClassVar[ValueSource]
    VALUE_SOURCE_REDIS: _ClassVar[ValueSource]
    VALUE_SOURCE_API: _ClassVar[ValueSource]
    VALUE_SOURCE_COMMAND_LINE: _ClassVar[ValueSource]
    VALUE_SOURCE_REMOTE: _ClassVar[ValueSource]
    VALUE_SOURCE_COMPUTED: _ClassVar[ValueSource]
    VALUE_SOURCE_INHERITED: _ClassVar[ValueSource]
    VALUE_SOURCE_OVERRIDE: _ClassVar[ValueSource]
    VALUE_SOURCE_CUSTOM: _ClassVar[ValueSource]

VALUE_SOURCE_UNSPECIFIED: ValueSource
VALUE_SOURCE_DEFAULT: ValueSource
VALUE_SOURCE_ENVIRONMENT: ValueSource
VALUE_SOURCE_FILE: ValueSource
VALUE_SOURCE_DATABASE: ValueSource
VALUE_SOURCE_CONSUL: ValueSource
VALUE_SOURCE_ETCD: ValueSource
VALUE_SOURCE_KUBERNETES: ValueSource
VALUE_SOURCE_VAULT: ValueSource
VALUE_SOURCE_AWS_PARAMETER_STORE: ValueSource
VALUE_SOURCE_AWS_SECRETS_MANAGER: ValueSource
VALUE_SOURCE_AZURE_KEY_VAULT: ValueSource
VALUE_SOURCE_GCP_SECRET_MANAGER: ValueSource
VALUE_SOURCE_REDIS: ValueSource
VALUE_SOURCE_API: ValueSource
VALUE_SOURCE_COMMAND_LINE: ValueSource
VALUE_SOURCE_REMOTE: ValueSource
VALUE_SOURCE_COMPUTED: ValueSource
VALUE_SOURCE_INHERITED: ValueSource
VALUE_SOURCE_OVERRIDE: ValueSource
VALUE_SOURCE_CUSTOM: ValueSource
