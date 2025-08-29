from gcommon.v1.media import media_quality_pb2 as _media_quality_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.media import audio_analysis_pb2 as _audio_analysis_pb2
from gcommon.v1.media import scene_detection_pb2 as _scene_detection_pb2
from gcommon.v1.media import technical_metadata_pb2 as _technical_metadata_pb2
from gcommon.v1.media import thumbnail_info_pb2 as _thumbnail_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaAnalysis(_message.Message):
    __slots__ = ("technical", "quality_analysis", "scenes", "thumbnails", "audio_analysis")
    TECHNICAL_FIELD_NUMBER: _ClassVar[int]
    QUALITY_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    SCENES_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    technical: _technical_metadata_pb2.TechnicalMetadata
    quality_analysis: _media_quality_pb2.MediaQuality
    scenes: _containers.RepeatedCompositeFieldContainer[_scene_detection_pb2.SceneDetection]
    thumbnails: _containers.RepeatedCompositeFieldContainer[_thumbnail_info_pb2.ThumbnailInfo]
    audio_analysis: _audio_analysis_pb2.AudioAnalysis
    def __init__(self, technical: _Optional[_Union[_technical_metadata_pb2.TechnicalMetadata, _Mapping]] = ..., quality_analysis: _Optional[_Union[_media_quality_pb2.MediaQuality, _Mapping]] = ..., scenes: _Optional[_Iterable[_Union[_scene_detection_pb2.SceneDetection, _Mapping]]] = ..., thumbnails: _Optional[_Iterable[_Union[_thumbnail_info_pb2.ThumbnailInfo, _Mapping]]] = ..., audio_analysis: _Optional[_Union[_audio_analysis_pb2.AudioAnalysis, _Mapping]] = ...) -> None: ...
