from gcommon.v1.media.enums import media_type_pb2 as _media_type_pb2
from gcommon.v1.media.messages import audio_track_pb2 as _audio_track_pb2
from gcommon.v1.media.messages import media_metadata_pb2 as _media_metadata_pb2
from gcommon.v1.media.messages import media_quality_pb2 as _media_quality_pb2
from gcommon.v1.media.messages import subtitle_track_pb2 as _subtitle_track_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaFile(_message.Message):
    __slots__ = ("id", "path", "filename", "type", "size_bytes", "created_at", "modified_at", "metadata", "subtitle_tracks", "audio_tracks", "quality")
    ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_TRACKS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TRACKS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    path: str
    filename: str
    type: _media_type_pb2.MediaType
    size_bytes: int
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    metadata: _media_metadata_pb2.MediaMetadata
    subtitle_tracks: _containers.RepeatedCompositeFieldContainer[_subtitle_track_pb2.SubtitleTrack]
    audio_tracks: _containers.RepeatedCompositeFieldContainer[_audio_track_pb2.AudioTrack]
    quality: _media_quality_pb2.MediaQuality
    def __init__(self, id: _Optional[str] = ..., path: _Optional[str] = ..., filename: _Optional[str] = ..., type: _Optional[_Union[_media_type_pb2.MediaType, str]] = ..., size_bytes: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Union[_media_metadata_pb2.MediaMetadata, _Mapping]] = ..., subtitle_tracks: _Optional[_Iterable[_Union[_subtitle_track_pb2.SubtitleTrack, _Mapping]]] = ..., audio_tracks: _Optional[_Iterable[_Union[_audio_track_pb2.AudioTrack, _Mapping]]] = ..., quality: _Optional[_Union[_media_quality_pb2.MediaQuality, _Mapping]] = ...) -> None: ...
