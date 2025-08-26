from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AnalyzeAudioQualityResponse(_message.Message):
    __slots__ = ("peak_level_db", "rms_level_db", "dynamic_range_db", "signal_to_noise_ratio", "clipping_detected")
    PEAK_LEVEL_DB_FIELD_NUMBER: _ClassVar[int]
    RMS_LEVEL_DB_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_RANGE_DB_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_TO_NOISE_RATIO_FIELD_NUMBER: _ClassVar[int]
    CLIPPING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    peak_level_db: float
    rms_level_db: float
    dynamic_range_db: float
    signal_to_noise_ratio: float
    clipping_detected: bool
    def __init__(self, peak_level_db: _Optional[float] = ..., rms_level_db: _Optional[float] = ..., dynamic_range_db: _Optional[float] = ..., signal_to_noise_ratio: _Optional[float] = ..., clipping_detected: _Optional[bool] = ...) -> None: ...
