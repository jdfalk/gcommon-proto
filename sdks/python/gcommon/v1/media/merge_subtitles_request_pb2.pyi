from gcommon.v1.media import merge_options_pb2 as _merge_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MergeSubtitlesRequest(_message.Message):
    __slots__ = ("subtitle_file_ids", "output_file_id", "merge_options")
    SUBTITLE_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    MERGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_ids: _containers.RepeatedScalarFieldContainer[str]
    output_file_id: str
    merge_options: _merge_options_pb2.MergeOptions
    def __init__(
        self,
        subtitle_file_ids: _Optional[_Iterable[str]] = ...,
        output_file_id: _Optional[str] = ...,
        merge_options: _Optional[
            _Union[_merge_options_pb2.MergeOptions, _Mapping]
        ] = ...,
    ) -> None: ...
