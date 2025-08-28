# media Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 11
- **Messages**: 19
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [audio_track.proto](#audio_track)
- [chapter_info.proto](#chapter_info)
- [media_analysis.proto](#media_analysis)
- [media_file.proto](#media_file)
- [media_metadata.proto](#media_metadata)
- [media_quality.proto](#media_quality)
- [merge_options.proto](#merge_options)
- [movie_info.proto](#movie_info)
- [series_info.proto](#series_info)
- [subtitle_track.proto](#subtitle_track)
- [transcode_options.proto](#transcode_options)
---


## Detailed Documentation

### audio_track.proto {#audio_track}

**Path**: `gcommon/v1/media/audio_track.proto` **Package**: `gcommon.v1.media` **Lines**: 25

**Messages** (1): `AudioTrack`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/audio_track.proto
// version: 1.0.0
// guid: 55a5a263-fb45-49ae-8090-81d826cc0a5f

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Audio track information.
message AudioTrack {
  int32 index = 1 [(buf.validate.field).int32.gte = 0];
  string language = 2 [(buf.validate.field).string.min_len = 1];
  string codec = 3 [(buf.validate.field).string.min_len = 1];
  string title = 4 [(buf.validate.field).string.min_len = 1];
  int32 channels = 5 [(buf.validate.field).int32.gte = 0];
  int32 sample_rate = 6 [(buf.validate.field).int32.gte = 0];
  bool default_track = 7;
}
```

---

### chapter_info.proto {#chapter_info}

**Path**: `gcommon/v1/media/chapter_info.proto` **Package**: `gcommon.v1.media` **Lines**: 23

**Messages** (1): `ChapterInfo`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/chapter_info.proto
// version: 1.0.1
// guid: 3456789-abcd-ef01-b0c1-d2e3f4a5b6c7

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Information about a chapter or segment.
message ChapterInfo {
  int32 index = 1; // Chapter number (1-based)
  string title = 2; // Chapter title
  google.protobuf.Duration start_time = 3; // Start time
  google.protobuf.Duration end_time = 4; // End time
  google.protobuf.Duration duration = 5; // Chapter duration
  string description = 6; // Chapter description/summary
}
```

---

### media_analysis.proto {#media_analysis}

**Path**: `gcommon/v1/media/media_analysis.proto` **Package**: `gcommon.v1.media` **Lines**: 99

**Messages** (9): `MediaAnalysis`, `TechnicalMetadata`, `VideoStreamInfo`, `AudioStreamInfo`, `SubtitleStreamInfo`, `SceneDetection`, `ThumbnailInfo`, `AudioAnalysis`, `SilentSegment`

**Imports** (4):

- `gcommon/v1/media/media_quality.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/media_analysis.proto
// version: 1.0.0
// guid: cdef012-3456-789a-c7d8-e9f0a1b2c3d4

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_quality.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Comprehensive media analysis results.
message MediaAnalysis {
  TechnicalMetadata technical = 1;
  MediaQuality quality_analysis = 2;
  repeated SceneDetection scenes = 3 [(buf.validate.field).repeated.min_items = 1];
  repeated ThumbnailInfo thumbnails = 4 [(buf.validate.field).repeated.min_items = 1];
  AudioAnalysis audio_analysis = 5;
}

// Technical metadata extracted from media.
message TechnicalMetadata {
  google.protobuf.Duration duration = 1;
  int64 file_size = 2 [(buf.validate.field).int64.gte = 0];
  int64 bitrate = 3 [(buf.validate.field).int64.gte = 0];
  string container_format = 4 [(buf.validate.field).string.min_len = 1];
  VideoStreamInfo video = 5;
  repeated AudioStreamInfo audio_streams = 6 [(buf.validate.field).repeated.min_items = 1];
  repeated SubtitleStreamInfo subtitle_streams = 7 [(buf.validate.field).repeated.min_items = 1];
}

// Video stream information.
message VideoStreamInfo {
  string codec = 1 [(buf.validate.field).string.min_len = 1];
  int32 width = 2 [(buf.validate.field).int32.gte = 0];
  int32 height = 3 [(buf.validate.field).int32.gte = 0];
  double frame_rate = 4 [(buf.validate.field).double.gte = 0.0];
  int64 bitrate = 5 [(buf.validate.field).int64.gte = 0];
  string pixel_format = 6 [(buf.validate.field).string.min_len = 1];
  string color_space = 7 [(buf.validate.field).string.min_len = 1];
}

// Audio stream information.
message AudioStreamInfo {
  int32 stream_index = 1 [(buf.validate.field).int32.gte = 0];
  string codec = 2 [(buf.validate.field).string.min_len = 1];
  int32 sample_rate = 3 [(buf.validate.field).int32.gte = 0];
  int32 channels = 4 [(buf.validate.field).int32.gte = 0];
  int64 bitrate = 5 [(buf.validate.field).int64.gte = 0];
  string language = 6 [(buf.validate.field).string.min_len = 1];
  string title = 7 [(buf.validate.field).string.min_len = 1];
}

// Subtitle stream information.
message SubtitleStreamInfo {
  int32 stream_index = 1 [(buf.validate.field).int32.gte = 0];
  string codec = 2 [(buf.validate.field).string.min_len = 1];
  string language = 3 [(buf.validate.field).string.min_len = 1];
  string title = 4 [(buf.validate.field).string.min_len = 1];
  bool forced = 5;
  bool hearing_impaired = 6;
}

// Scene detection results.
message SceneDetection {
  google.protobuf.Duration start_time = 1;
  google.protobuf.Duration end_time = 2;
  double confidence = 3 [(buf.validate.field).double.gte = 0.0];
  string scene_type = 4; // dialog, action, credits, etc.
}

// Thumbnail information.
message ThumbnailInfo {
  google.protobuf.Duration timestamp = 1;
  string file_path = 2 [(buf.validate.field).string.min_len = 1];
  int32 width = 3 [(buf.validate.field).int32.gte = 0];
  int32 height = 4 [(buf.validate.field).int32.gte = 0];
}

// Audio analysis results.
message AudioAnalysis {
  double peak_level = 1; // Peak audio level in dB
  double rms_level = 2; // RMS audio level in dB
  repeated SilentSegment silent_segments = 3 [(buf.validate.field).repeated.min_items = 1];
  double dynamic_range = 4; // Dynamic range in dB
}

// Silent audio segments.
message SilentSegment {
  google.protobuf.Duration start_time = 1;
  google.protobuf.Duration end_time = 2;
  double threshold_db = 3; // Silence threshold used
}
```

---

### media_file.proto {#media_file}

**Path**: `gcommon/v1/media/media_file.proto` **Package**: `gcommon.v1.media` **Lines**: 37

**Messages** (1): `MediaFile`

**Imports** (8):

- `gcommon/v1/common/media_type.proto`
- `gcommon/v1/media/audio_track.proto`
- `gcommon/v1/media/media_metadata.proto`
- `gcommon/v1/media/media_quality.proto`
- `gcommon/v1/media/subtitle_track.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/media_file.proto
// version: 1.0.0
// guid: e3bc9175-1261-4755-9d32-d991586e723f

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/common/media_type.proto";
import "gcommon/v1/media/audio_track.proto";
import "gcommon/v1/media/media_metadata.proto";
import "gcommon/v1/media/media_quality.proto";
import "gcommon/v1/media/subtitle_track.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Media file representation with associated metadata and tracks.
message MediaFile {
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
  string path = 2;
  string filename = 3;
  gcommon.v1.common.MediaType type = 4;
  int64 size_bytes = 5;
  google.protobuf.Timestamp created_at = 6 [lazy = true, (buf.validate.field).required = true];
  google.protobuf.Timestamp modified_at = 7 [lazy = true];
  MediaMetadata metadata = 8;
  repeated SubtitleTrack subtitle_tracks = 9;
  repeated AudioTrack audio_tracks = 10;
  MediaQuality quality = 11;
}
```

---

### media_metadata.proto {#media_metadata}

**Path**: `gcommon/v1/media/media_metadata.proto` **Package**: `gcommon.v1.media` **Lines**: 33

**Messages** (1): `MediaMetadata`

**Imports** (4):

- `gcommon/v1/media/movie_info.proto`
- `gcommon/v1/media/series_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/metadata/media_metadata.proto
// version: 1.0.0
// guid: e5b804c2-185f-402f-8edb-b3c390406e52

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/movie_info.proto";
import "gcommon/v1/media/series_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Metadata information for a media file from external sources.
message MediaMetadata {
  string title = 1 [(buf.validate.field).string.min_len = 1];
  string original_title = 2 [(buf.validate.field).string.min_len = 1];
  int32 year = 3 [(buf.validate.field).int32.gte = 0];
  string plot = 4 [(buf.validate.field).string.min_len = 1];
  repeated string genres = 5 [(buf.validate.field).repeated.min_items = 1];
  string imdb_id = 6 [(buf.validate.field).string.min_len = 1];
  string tmdb_id = 7 [(buf.validate.field).string.min_len = 1];
  float rating = 8 [(buf.validate.field).float.gte = 0.0];
  repeated string languages = 9 [(buf.validate.field).repeated.min_items = 1];
  repeated string actors = 10 [(buf.validate.field).repeated.min_items = 1];
  repeated string directors = 11 [(buf.validate.field).repeated.min_items = 1];
  SeriesInfo series_info = 12;
  MovieInfo movie_info = 13;
}
```

---

### media_quality.proto {#media_quality}

**Path**: `gcommon/v1/media/media_quality.proto` **Package**: `gcommon.v1.media` **Lines**: 25

**Messages** (1): `MediaQuality`

**Imports** (4):

- `gcommon/v1/common/quality_score.proto`
- `gcommon/v1/common/resolution.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/media_quality.proto
// version: 1.0.0
// guid: 62c527ab-9d69-4c5c-af80-64aa0657f948

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/common/quality_score.proto";
import "gcommon/v1/common/resolution.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Media quality assessment.
message MediaQuality {
  gcommon.v1.common.Resolution resolution = 1;
  string video_codec = 2 [(buf.validate.field).string.min_len = 1];
  int32 bitrate_kbps = 3 [(buf.validate.field).int32.gte = 0];
  float duration_seconds = 4 [(buf.validate.field).float.gte = 0.0];
  gcommon.v1.common.QualityScore quality_score = 5;
}
```

---

### merge_options.proto {#merge_options}

**Path**: `gcommon/v1/media/merge_options.proto` **Package**: `gcommon.v1.media` **Lines**: 21

**Messages** (1): `MergeOptions`

**Imports** (2):

- `gcommon/v1/common/conflict_resolution.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/merge_options.proto
// version: 1.0.1
// guid: 789abcde-f012-3456-7890-abcdef123456

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/common/conflict_resolution.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Options for merging subtitles.
message MergeOptions {
  string output_format = 1; // Output format (srt, vtt, ass, etc.)
  bool preserve_formatting = 2; // Keep original formatting
  gcommon.v1.common.ConflictResolution conflict_resolution = 3; // How to handle overlapping subtitles
  bool sort_by_timestamp = 4; // Sort merged subtitles by timestamp
}
```

---

### movie_info.proto {#movie_info}

**Path**: `gcommon/v1/media/movie_info.proto` **Package**: `gcommon.v1.media` **Lines**: 23

**Messages** (1): `MovieInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/metadata/movie_info.proto
// version: 1.0.0
// guid: fc3b809f-03e7-4446-b355-e7482000e343

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Movie specific information.
message MovieInfo {
  google.protobuf.Timestamp release_date = 1;
  int64 budget = 2 [(buf.validate.field).int64.gte = 0];
  int64 revenue = 3 [(buf.validate.field).int64.gte = 0];
  int32 runtime_minutes = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### series_info.proto {#series_info}

**Path**: `gcommon/v1/media/series_info.proto` **Package**: `gcommon.v1.media` **Lines**: 26

**Messages** (1): `SeriesInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/metadata/series_info.proto
// version: 1.0.0
// guid: 1ff30d9b-8171-4cb2-885c-0ae98bd2ad17

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// TV series specific information.
message SeriesInfo {
  int32 season = 1;
  int32 episode = 2;
  string series_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  string episode_title = 4;
  google.protobuf.Timestamp air_date = 5;
}
```

---

### subtitle_track.proto {#subtitle_track}

**Path**: `gcommon/v1/media/subtitle_track.proto` **Package**: `gcommon.v1.media` **Lines**: 25

**Messages** (1): `SubtitleTrack`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/subtitle_track.proto
// version: 1.0.0
// guid: 2c899982-81d3-43b7-a542-24361cdef856

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Subtitle track information.
message SubtitleTrack {
  int32 index = 1 [(buf.validate.field).int32.gte = 0];
  string language = 2 [(buf.validate.field).string.min_len = 1];
  string codec = 3 [(buf.validate.field).string.min_len = 1];
  string title = 4 [(buf.validate.field).string.min_len = 1];
  bool forced = 5;
  bool hearing_impaired = 6;
  bool default_track = 7;
}
```

---

### transcode_options.proto {#transcode_options}

**Path**: `gcommon/v1/media/transcode_options.proto` **Package**: `gcommon.v1.media` **Lines**: 23

**Messages** (1): `TranscodeOptions`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/transcode_options.proto
// version: 1.0.1
// guid: a1b2c3d4-e5f6-7890-1234-567890abcdef

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Transcoding options.
message TranscodeOptions {
  string resolution = 1; // Target resolution (1920x1080, 1280x720, etc.)
  int32 bitrate = 2; // Target bitrate in kbps
  int32 framerate = 3; // Target framerate
  string audio_codec = 4; // Audio codec (aac, mp3, ac3, etc.)
  int32 audio_bitrate = 5; // Audio bitrate in kbps
  bool preserve_subtitles = 6; // Keep subtitle tracks
  bool preserve_chapters = 7; // Keep chapter markers
}
```

---

