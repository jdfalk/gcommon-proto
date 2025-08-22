from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_TYPE_UNSPECIFIED: _ClassVar[MediaType]
    MEDIA_TYPE_MOVIE: _ClassVar[MediaType]
    MEDIA_TYPE_TV_EPISODE: _ClassVar[MediaType]
    MEDIA_TYPE_DOCUMENTARY: _ClassVar[MediaType]
    MEDIA_TYPE_ANIME: _ClassVar[MediaType]
    MEDIA_TYPE_AUDIOBOOK: _ClassVar[MediaType]
    MEDIA_TYPE_PODCAST: _ClassVar[MediaType]
    MEDIA_TYPE_MUSIC: _ClassVar[MediaType]
    MEDIA_TYPE_LECTURE: _ClassVar[MediaType]
    MEDIA_TYPE_INTERVIEW: _ClassVar[MediaType]
    MEDIA_TYPE_RADIO_SHOW: _ClassVar[MediaType]
MEDIA_TYPE_UNSPECIFIED: MediaType
MEDIA_TYPE_MOVIE: MediaType
MEDIA_TYPE_TV_EPISODE: MediaType
MEDIA_TYPE_DOCUMENTARY: MediaType
MEDIA_TYPE_ANIME: MediaType
MEDIA_TYPE_AUDIOBOOK: MediaType
MEDIA_TYPE_PODCAST: MediaType
MEDIA_TYPE_MUSIC: MediaType
MEDIA_TYPE_LECTURE: MediaType
MEDIA_TYPE_INTERVIEW: MediaType
MEDIA_TYPE_RADIO_SHOW: MediaType
