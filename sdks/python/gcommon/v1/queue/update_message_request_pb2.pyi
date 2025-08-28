from gcommon.v1.queue import content_update_pb2 as _content_update_pb2
from gcommon.v1.queue import message_update_properties_pb2 as _message_update_properties_pb2
from gcommon.v1.queue import metadata_update_pb2 as _metadata_update_pb2
from gcommon.v1.queue import priority_update_pb2 as _priority_update_pb2
from gcommon.v1.queue import update_condition_pb2 as _update_condition_pb2
from gcommon.v1.queue import visibility_update_pb2 as _visibility_update_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateMessageRequest(_message.Message):
    __slots__ = ("message_id", "topic", "partition_id", "message_offset", "properties", "visibility_update", "priority_update", "metadata_update", "content_update", "update_fields", "condition", "operation_metadata")
    class OperationMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    topic: str
    partition_id: int
    message_offset: int
    properties: _message_update_properties_pb2.MessageUpdateProperties
    visibility_update: _visibility_update_pb2.VisibilityUpdate
    priority_update: _priority_update_pb2.PriorityUpdate
    metadata_update: _metadata_update_pb2.MetadataUpdate
    content_update: _content_update_pb2.ContentUpdate
    update_fields: _containers.RepeatedScalarFieldContainer[str]
    condition: _update_condition_pb2.UpdateCondition
    operation_metadata: _containers.ScalarMap[str, str]
    def __init__(self, message_id: _Optional[str] = ..., topic: _Optional[str] = ..., partition_id: _Optional[int] = ..., message_offset: _Optional[int] = ..., properties: _Optional[_Union[_message_update_properties_pb2.MessageUpdateProperties, _Mapping]] = ..., visibility_update: _Optional[_Union[_visibility_update_pb2.VisibilityUpdate, _Mapping]] = ..., priority_update: _Optional[_Union[_priority_update_pb2.PriorityUpdate, _Mapping]] = ..., metadata_update: _Optional[_Union[_metadata_update_pb2.MetadataUpdate, _Mapping]] = ..., content_update: _Optional[_Union[_content_update_pb2.ContentUpdate, _Mapping]] = ..., update_fields: _Optional[_Iterable[str]] = ..., condition: _Optional[_Union[_update_condition_pb2.UpdateCondition, _Mapping]] = ..., operation_metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
