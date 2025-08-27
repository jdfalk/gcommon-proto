from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from gcommon.v1.queue import received_message_pb2 as _received_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PullResponse(_message.Message):
    __slots__ = ("message", "metadata")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    message: _received_message_pb2.ReceivedMessage
    metadata: _response_metadata_pb2.ResponseMetadata
    def __init__(
        self,
        message: _Optional[
            _Union[_received_message_pb2.ReceivedMessage, _Mapping]
        ] = ...,
        metadata: _Optional[
            _Union[_response_metadata_pb2.ResponseMetadata, _Mapping]
        ] = ...,
    ) -> None: ...
