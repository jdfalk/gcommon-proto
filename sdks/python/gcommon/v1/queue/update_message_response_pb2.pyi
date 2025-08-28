from gcommon.v1.queue import failed_field_update_pb2 as _failed_field_update_pb2
from gcommon.v1.queue import updated_properties_pb2 as _updated_properties_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateMessageResponse(_message.Message):
    __slots__ = ("success", "message_id", "new_version", "updated_at", "updated_fields", "failed_fields", "error_message", "error_code", "warnings", "updated_properties", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message_id: str
    new_version: str
    updated_at: _timestamp_pb2.Timestamp
    updated_fields: _containers.RepeatedScalarFieldContainer[str]
    failed_fields: _containers.RepeatedCompositeFieldContainer[_failed_field_update_pb2.FailedFieldUpdate]
    error_message: str
    error_code: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    updated_properties: _updated_properties_pb2.UpdatedProperties
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, success: bool = ..., message_id: _Optional[str] = ..., new_version: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_fields: _Optional[_Iterable[str]] = ..., failed_fields: _Optional[_Iterable[_Union[_failed_field_update_pb2.FailedFieldUpdate, _Mapping]]] = ..., error_message: _Optional[str] = ..., error_code: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ..., updated_properties: _Optional[_Union[_updated_properties_pb2.UpdatedProperties, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
