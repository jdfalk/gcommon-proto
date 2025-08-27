from gcommon.v1.queue import node_info_pb2 as _node_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetNodeInfoResponse(_message.Message):
    __slots__ = ("node_info", "success", "error")
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    node_info: _node_info_pb2.NodeInfo
    success: bool
    error: str
    def __init__(
        self,
        node_info: _Optional[_Union[_node_info_pb2.NodeInfo, _Mapping]] = ...,
        success: _Optional[bool] = ...,
        error: _Optional[str] = ...,
    ) -> None: ...
