from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.queue import delete_criteria_pb2 as _delete_criteria_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueDeleteRequest(_message.Message):
    __slots__ = (
        "queue_name",
        "message_id",
        "ack_token",
        "force",
        "reason",
        "criteria",
        "metadata",
    )
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    message_id: str
    ack_token: str
    force: bool
    reason: str
    criteria: _delete_criteria_pb2.DeleteCriteria
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(
        self,
        queue_name: _Optional[str] = ...,
        message_id: _Optional[str] = ...,
        ack_token: _Optional[str] = ...,
        force: _Optional[bool] = ...,
        reason: _Optional[str] = ...,
        criteria: _Optional[
            _Union[_delete_criteria_pb2.DeleteCriteria, _Mapping]
        ] = ...,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
    ) -> None: ...
