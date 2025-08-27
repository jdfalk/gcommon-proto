import datetime

from gcommon.v1.config import config_diff_entry_pb2 as _config_diff_entry_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigDiff(_message.Message):
    __slots__ = (
        "diff_id",
        "source_version",
        "target_version",
        "added",
        "modified",
        "removed",
        "computed_at",
        "requested_by",
        "metadata",
    )
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    DIFF_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    ADDED_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    COMPUTED_AT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    diff_id: str
    source_version: str
    target_version: str
    added: _containers.RepeatedCompositeFieldContainer[
        _config_diff_entry_pb2.ConfigDiffEntry
    ]
    modified: _containers.RepeatedCompositeFieldContainer[
        _config_diff_entry_pb2.ConfigDiffEntry
    ]
    removed: _containers.RepeatedCompositeFieldContainer[
        _config_diff_entry_pb2.ConfigDiffEntry
    ]
    computed_at: _timestamp_pb2.Timestamp
    requested_by: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(
        self,
        diff_id: _Optional[str] = ...,
        source_version: _Optional[str] = ...,
        target_version: _Optional[str] = ...,
        added: _Optional[
            _Iterable[_Union[_config_diff_entry_pb2.ConfigDiffEntry, _Mapping]]
        ] = ...,
        modified: _Optional[
            _Iterable[_Union[_config_diff_entry_pb2.ConfigDiffEntry, _Mapping]]
        ] = ...,
        removed: _Optional[
            _Iterable[_Union[_config_diff_entry_pb2.ConfigDiffEntry, _Mapping]]
        ] = ...,
        computed_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        requested_by: _Optional[str] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
