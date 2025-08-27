from gcommon.v1.queue import partition_info_pb2 as _partition_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPartitionInfoResponse(_message.Message):
    __slots__ = ("partition_info", "success", "error")
    PARTITION_INFO_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    partition_info: _partition_info_pb2.PartitionInfo
    success: bool
    error: str
    def __init__(
        self,
        partition_info: _Optional[
            _Union[_partition_info_pb2.PartitionInfo, _Mapping]
        ] = ...,
        success: _Optional[bool] = ...,
        error: _Optional[str] = ...,
    ) -> None: ...
