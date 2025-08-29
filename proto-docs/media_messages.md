# Media Messages Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 55
- **Messages**: 71

## Table of Contents

### Messages

- [`AdjustSubtitleTimingRequest`](#adjust_subtitle_timing_request) - from adjust_subtitle_timing_request.proto
- [`AdjustSubtitleTimingResponse`](#adjust_subtitle_timing_response) - from adjust_subtitle_timing_response.proto
- [`AnalysisOptions`](#analyze_media_request) - from analyze_media_request.proto
- [`AnalyzeAudioQualityRequest`](#analyze_audio_quality_request) - from analyze_audio_quality_request.proto
- [`AnalyzeAudioQualityResponse`](#analyze_audio_quality_response) - from analyze_audio_quality_response.proto
- [`AnalyzeMediaRequest`](#analyze_media_request) - from analyze_media_request.proto
- [`AnalyzeMediaResponse`](#analyze_media_response) - from analyze_media_response.proto
- [`AudioAnalysis`](#media_analysis) - from media_analysis.proto
- [`AudioExtractionOptions`](#extract_audio_request) - from extract_audio_request.proto
- [`AudioStreamInfo`](#media_analysis) - from media_analysis.proto
- [`AudioTrack`](#audio_track) - from audio_track.proto
- [`ChapterDetectionOptions`](#detect_chapters_request) - from detect_chapters_request.proto
- [`ChapterInfo`](#chapter_info) - from chapter_info.proto
- [`ConvertSubtitleFormatRequest`](#convert_subtitle_format_request) - from convert_subtitle_format_request.proto
- [`ConvertSubtitleFormatResponse`](#convert_subtitle_format_response) - from convert_subtitle_format_response.proto
- [`CreateMediaFileRequest`](#create_media_file_request) - from create_media_file_request.proto
- [`CreateMediaFileResponse`](#create_media_file_response) - from create_media_file_response.proto
- [`DeleteMediaFileRequest`](#delete_media_file_request) - from delete_media_file_request.proto
- [`DeleteMediaFileResponse`](#delete_media_file_response) - from delete_media_file_response.proto
- [`DetectChaptersRequest`](#detect_chapters_request) - from detect_chapters_request.proto
- [`DetectChaptersResponse`](#detect_chapters_response) - from detect_chapters_response.proto
- [`ExtractAudioRequest`](#extract_audio_request) - from extract_audio_request.proto
- [`ExtractAudioResponse`](#extract_audio_response) - from extract_audio_response.proto
- [`ExtractSubtitlesRequest`](#extract_subtitles_request) - from extract_subtitles_request.proto
- [`ExtractSubtitlesResponse`](#extract_subtitles_response) - from extract_subtitles_response.proto
- [`ExtractedSubtitle`](#extract_subtitles_response) - from extract_subtitles_response.proto
- [`GetMediaFileRequest`](#get_media_file_request) - from get_media_file_request.proto
- [`GetMediaFileResponse`](#get_media_file_response) - from get_media_file_response.proto
- [`GetProcessingStatusRequest`](#get_processing_status_request) - from get_processing_status_request.proto
- [`GetProcessingStatusResponse`](#get_processing_status_response) - from get_processing_status_response.proto
- [`ListMediaFilesRequest`](#list_media_files_request) - from list_media_files_request.proto
- [`ListMediaFilesResponse`](#list_media_files_response) - from list_media_files_response.proto
- [`MediaAnalysis`](#media_analysis) - from media_analysis.proto
- [`MediaFile`](#media_file) - from media_file.proto
- [`MediaMetadata`](#media_metadata) - from media_metadata.proto
- [`MediaQuality`](#media_quality) - from media_quality.proto
- [`MergeAudioRequest`](#merge_audio_request) - from merge_audio_request.proto
- [`MergeAudioResponse`](#merge_audio_response) - from merge_audio_response.proto
- [`MergeOptions`](#merge_options) - from merge_options.proto
- [`MergeSubtitlesRequest`](#merge_subtitles_request) - from merge_subtitles_request.proto
- [`MergeSubtitlesResponse`](#merge_subtitles_response) - from merge_subtitles_response.proto
- [`MovieInfo`](#movie_info) - from movie_info.proto
- [`NormalizationOptions`](#normalize_audio_request) - from normalize_audio_request.proto
- [`NormalizeAudioRequest`](#normalize_audio_request) - from normalize_audio_request.proto
- [`NormalizeAudioResponse`](#normalize_audio_response) - from normalize_audio_response.proto
- [`SceneDetection`](#media_analysis) - from media_analysis.proto
- [`SearchMediaRequest`](#search_media_request) - from search_media_request.proto
- [`SearchMediaResponse`](#search_media_response) - from search_media_response.proto
- [`SeriesInfo`](#series_info) - from series_info.proto
- [`SilentSegment`](#media_analysis) - from media_analysis.proto
- [`SplitAudioRequest`](#split_audio_request) - from split_audio_request.proto
- [`SplitAudioResponse`](#split_audio_response) - from split_audio_response.proto
- [`SplitPoint`](#split_audio_request) - from split_audio_request.proto
- [`SubtitleExtractionOptions`](#extract_subtitles_request) - from extract_subtitles_request.proto
- [`SubtitleStreamInfo`](#media_analysis) - from media_analysis.proto
- [`SubtitleTrack`](#subtitle_track) - from subtitle_track.proto
- [`SyncSubtitlesRequest`](#sync_subtitles_request) - from sync_subtitles_request.proto
- [`SyncSubtitlesResponse`](#sync_subtitles_response) - from sync_subtitles_response.proto
- [`TechnicalMetadata`](#media_analysis) - from media_analysis.proto
- [`ThumbnailInfo`](#media_analysis) - from media_analysis.proto
- [`TranscodeMediaRequest`](#transcode_media_request) - from transcode_media_request.proto
- [`TranscodeMediaResponse`](#transcode_media_response) - from transcode_media_response.proto
- [`TranscodeOptions`](#transcode_options) - from transcode_options.proto
- [`UpdateMediaFileRequest`](#update_media_file_request) - from update_media_file_request.proto
- [`UpdateMediaFileResponse`](#update_media_file_response) - from update_media_file_response.proto
- [`UploadMediaRequest`](#upload_media_request) - from upload_media_request.proto
- [`UploadMediaResponse`](#upload_media_response) - from upload_media_response.proto
- [`UploadMetadata`](#upload_media_request) - from upload_media_request.proto
- [`ValidateSubtitlesRequest`](#validate_subtitles_request) - from validate_subtitles_request.proto
- [`ValidateSubtitlesResponse`](#validate_subtitles_response) - from validate_subtitles_response.proto
- [`VideoStreamInfo`](#media_analysis) - from media_analysis.proto

### Files in this Module

- [adjust_subtitle_timing_request.proto](#adjust_subtitle_timing_request)
- [adjust_subtitle_timing_response.proto](#adjust_subtitle_timing_response)
- [analyze_audio_quality_request.proto](#analyze_audio_quality_request)
- [analyze_audio_quality_response.proto](#analyze_audio_quality_response)
- [analyze_media_request.proto](#analyze_media_request)
- [analyze_media_response.proto](#analyze_media_response)
- [convert_subtitle_format_request.proto](#convert_subtitle_format_request)
- [convert_subtitle_format_response.proto](#convert_subtitle_format_response)
- [create_media_file_request.proto](#create_media_file_request)
- [create_media_file_response.proto](#create_media_file_response)
- [delete_media_file_request.proto](#delete_media_file_request)
- [delete_media_file_response.proto](#delete_media_file_response)
- [detect_chapters_request.proto](#detect_chapters_request)
- [detect_chapters_response.proto](#detect_chapters_response)
- [extract_audio_request.proto](#extract_audio_request)
- [extract_audio_response.proto](#extract_audio_response)
- [extract_subtitles_request.proto](#extract_subtitles_request)
- [extract_subtitles_response.proto](#extract_subtitles_response)
- [get_media_file_request.proto](#get_media_file_request)
- [get_media_file_response.proto](#get_media_file_response)
- [get_processing_status_request.proto](#get_processing_status_request)
- [get_processing_status_response.proto](#get_processing_status_response)
- [list_media_files_request.proto](#list_media_files_request)
- [list_media_files_response.proto](#list_media_files_response)
- [merge_audio_request.proto](#merge_audio_request)
- [merge_audio_response.proto](#merge_audio_response)
- [merge_subtitles_request.proto](#merge_subtitles_request)
- [merge_subtitles_response.proto](#merge_subtitles_response)
- [normalize_audio_request.proto](#normalize_audio_request)
- [normalize_audio_response.proto](#normalize_audio_response)
- [search_media_request.proto](#search_media_request)
- [search_media_response.proto](#search_media_response)
- [split_audio_request.proto](#split_audio_request)
- [split_audio_response.proto](#split_audio_response)
- [sync_subtitles_request.proto](#sync_subtitles_request)
- [sync_subtitles_response.proto](#sync_subtitles_response)
- [transcode_media_request.proto](#transcode_media_request)
- [transcode_media_response.proto](#transcode_media_response)
- [update_media_file_request.proto](#update_media_file_request)
- [update_media_file_response.proto](#update_media_file_response)
- [upload_media_request.proto](#upload_media_request)
- [upload_media_response.proto](#upload_media_response)
- [validate_subtitles_request.proto](#validate_subtitles_request)
- [validate_subtitles_response.proto](#validate_subtitles_response)
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


## Messages Documentation

### adjust_subtitle_timing_request.proto {#adjust_subtitle_timing_request}

**Path**: `gcommon/v1/media/adjust_subtitle_timing_request.proto` **Package**: `gcommon.v1.media` **Lines**: 21

**Messages** (1): `AdjustSubtitleTimingRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/adjust_subtitle_timing_request.proto
// version: 1.0.0
// guid: 678901bc-def0-1234-a7b8-c9d0e1f23456

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to adjust subtitle timing.
message AdjustSubtitleTimingRequest {
  string subtitle_file_id = 1 [(buf.validate.field).string.min_len = 1];
  int64 time_offset_ms = 2; // Offset in milliseconds (positive or negative)
  bool preserve_duration = 3; // Whether to keep subtitle duration unchanged
}
```

---

### adjust_subtitle_timing_response.proto {#adjust_subtitle_timing_response}

**Path**: `gcommon/v1/media/adjust_subtitle_timing_response.proto` **Package**: `gcommon.v1.media` **Lines**: 21

**Messages** (1): `AdjustSubtitleTimingResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/adjust_subtitle_timing_response.proto
// version: 1.0.0
// guid: 789012cd-ef01-2345-b8c9-d0e1f2345678

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from adjusting subtitle timing.
message AdjustSubtitleTimingResponse {
  string adjusted_subtitle_file_id = 1 [(buf.validate.field).string.min_len = 1];
  bool success = 2;
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### analyze_audio_quality_request.proto {#analyze_audio_quality_request}

**Path**: `gcommon/v1/media/analyze_audio_quality_request.proto` **Package**: `gcommon.v1.media` **Lines**: 18

**Messages** (1): `AnalyzeAudioQualityRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/analyze_audio_quality_request.proto
// version: 1.0.0
// guid: abcdef0-1234-5678-c7d8-e9f0a1b2c3d4

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

message AnalyzeAudioQualityRequest {
  string audio_file_id = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### analyze_audio_quality_response.proto {#analyze_audio_quality_response}

**Path**: `gcommon/v1/media/analyze_audio_quality_response.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `AnalyzeAudioQualityResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/analyze_audio_quality_response.proto
// version: 1.0.0
// guid: bcdef01-2345-6789-d8e9-f0a1b2c3d4e5

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

message AnalyzeAudioQualityResponse {
  double peak_level_db = 1 [(buf.validate.field).double.gte = 0.0];
  double rms_level_db = 2 [(buf.validate.field).double.gte = 0.0];
  double dynamic_range_db = 3 [(buf.validate.field).double.gte = 0.0];
  double signal_to_noise_ratio = 4 [(buf.validate.field).double.gte = 0.0];
  bool clipping_detected = 5;
}
```

---

### analyze_media_request.proto {#analyze_media_request}

**Path**: `gcommon/v1/media/analyze_media_request.proto` **Package**: `gcommon.v1.media` **Lines**: 29

**Messages** (2): `AnalyzeMediaRequest`, `AnalysisOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/analyze_media_request.proto
// version: 1.0.0
// guid: abcdef0-1234-5678-a5b6-c7d8e9f0a1b2

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to analyze media content.
message AnalyzeMediaRequest {
  string media_file_id = 1 [(buf.validate.field).string.min_len = 1];
  AnalysisOptions options = 2;
}

// Analysis options.
message AnalysisOptions {
  bool extract_metadata = 1; // Extract technical metadata
  bool analyze_quality = 2; // Perform quality analysis
  bool detect_scenes = 3; // Scene detection
  bool extract_thumbnails = 4; // Generate thumbnail images
  bool analyze_audio = 5; // Audio analysis (levels, silence, etc.)
}
```

---

### analyze_media_response.proto {#analyze_media_response}

**Path**: `gcommon/v1/media/analyze_media_response.proto` **Package**: `gcommon.v1.media` **Lines**: 23

**Messages** (1): `AnalyzeMediaResponse`

**Imports** (3):

- `gcommon/v1/media/media_analysis.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/analyze_media_response.proto
// version: 1.0.0
// guid: bcdef01-2345-6789-b6c7-d8e9f0a1b2c3

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_analysis.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from media analysis.
message AnalyzeMediaResponse {
  string job_id = 1 [(buf.validate.field).string.min_len = 1];
  string status = 2; // pending, processing, completed, failed
  MediaAnalysis analysis = 3; // Analysis results (when completed)
  string error_message = 4; // Error details if failed
}
```

---

### convert_subtitle_format_request.proto {#convert_subtitle_format_request}

**Path**: `gcommon/v1/media/convert_subtitle_format_request.proto` **Package**: `gcommon.v1.media` **Lines**: 21

**Messages** (1): `ConvertSubtitleFormatRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/convert_subtitle_format_request.proto
// version: 1.0.0
// guid: 890123de-f012-3456-c9d0-e1f234567890

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to convert subtitle format.
message ConvertSubtitleFormatRequest {
  string subtitle_file_id = 1 [(buf.validate.field).string.min_len = 1];
  string target_format = 2; // Target format (srt, vtt, ass, etc.)
  bool preserve_styling = 3; // Whether to preserve styling information
}
```

---

### convert_subtitle_format_response.proto {#convert_subtitle_format_response}

**Path**: `gcommon/v1/media/convert_subtitle_format_response.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `ConvertSubtitleFormatResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/convert_subtitle_format_response.proto
// version: 1.0.0
// guid: 345678cd-ef01-2345-f6a7-b8c9d0e1f234

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from converting subtitle format.
message ConvertSubtitleFormatResponse {
  string converted_subtitle_file_id = 1 [(buf.validate.field).string.min_len = 1];
  bool success = 2;
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
  string output_format = 4; // The format the file was converted to
}
```

---

### create_media_file_request.proto {#create_media_file_request}

**Path**: `gcommon/v1/media/create_media_file_request.proto` **Package**: `gcommon.v1.media` **Lines**: 18

**Messages** (1): `CreateMediaFileRequest`

**Imports** (2):

- `gcommon/v1/media/media_file.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/create_media_file_request.proto
// version: 1.0.1
// guid: 3a4b5c6d-7e8f-9012-b3c4-d5e6f7a8b9c0

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_file.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to create a media file record.
message CreateMediaFileRequest {
  MediaFile media_file = 1;
}
```

---

### create_media_file_response.proto {#create_media_file_response}

**Path**: `gcommon/v1/media/create_media_file_response.proto` **Package**: `gcommon.v1.media` **Lines**: 18

**Messages** (1): `CreateMediaFileResponse`

**Imports** (2):

- `gcommon/v1/media/media_file.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/create_media_file_response.proto
// version: 1.0.1
// guid: 4b5c6d7e-8f90-1234-c5d6-e7f8a9b0c1d2

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_file.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from creating a media file record.
message CreateMediaFileResponse {
  MediaFile media_file = 1;
}
```

---

### delete_media_file_request.proto {#delete_media_file_request}

**Path**: `gcommon/v1/media/delete_media_file_request.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `DeleteMediaFileRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/delete_media_file_request.proto
// version: 1.0.0
// guid: 9012345-6789-0123-b4c5-d6e7f8a9b0c1

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to delete a media file.
message DeleteMediaFileRequest {
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
  bool delete_from_storage = 2; // Also delete the physical file
}
```

---

### delete_media_file_response.proto {#delete_media_file_response}

**Path**: `gcommon/v1/media/delete_media_file_response.proto` **Package**: `gcommon.v1.media` **Lines**: 17

**Messages** (1): `DeleteMediaFileResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/delete_media_file_response.proto
// version: 1.0.1
// guid: 0123456-789a-bcde-c5d6-e7f8a9b0c1d2

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from deleting a media file.
message DeleteMediaFileResponse {
  bool success = 1;
}
```

---

### detect_chapters_request.proto {#detect_chapters_request}

**Path**: `gcommon/v1/media/detect_chapters_request.proto` **Package**: `gcommon.v1.media` **Lines**: 28

**Messages** (2): `DetectChaptersRequest`, `ChapterDetectionOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/detect_chapters_request.proto
// version: 1.0.0
// guid: 1234567-89ab-cdef-f8a9-b0c1d2e3f4a5

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to detect chapters in audio content.
message DetectChaptersRequest {
  string audio_file_id = 1 [(buf.validate.field).string.min_len = 1];
  ChapterDetectionOptions options = 2;
}

// Options for chapter detection.
message ChapterDetectionOptions {
  double silence_threshold_db = 1; // Silence threshold in dB
  double min_chapter_length_seconds = 2; // Minimum chapter length
  bool use_metadata = 3; // Use existing metadata for hints
  bool use_ai_detection = 4; // Use AI-based scene detection
}
```

---

### detect_chapters_response.proto {#detect_chapters_response}

**Path**: `gcommon/v1/media/detect_chapters_response.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `DetectChaptersResponse`

**Imports** (3):

- `gcommon/v1/media/chapter_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/detect_chapters_response.proto
// version: 1.0.0
// guid: 2345678-9abc-def0-a9b0-c1d2e3f4a5b6

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/chapter_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from chapter detection.
message DetectChaptersResponse {
  repeated ChapterInfo chapters = 1 [(buf.validate.field).repeated.min_items = 1];
  int32 total_chapters = 2 [(buf.validate.field).int32.gte = 0];
  double confidence_score = 3; // Overall confidence in detection (0.0-1.0)
}
```

---

### extract_audio_request.proto {#extract_audio_request}

**Path**: `gcommon/v1/media/extract_audio_request.proto` **Package**: `gcommon.v1.media` **Lines**: 29

**Messages** (2): `ExtractAudioRequest`, `AudioExtractionOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/extract_audio_request.proto
// version: 1.0.0
// guid: def0123-4567-89ab-d8e9-f0a1b2c3d4e5

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to extract audio tracks from media.
message ExtractAudioRequest {
  string media_file_id = 1 [(buf.validate.field).string.min_len = 1];
  repeated int32 track_indices = 2; // Specific tracks to extract (empty = all)
  AudioExtractionOptions options = 3;
}

// Audio extraction options.
message AudioExtractionOptions {
  string output_format = 1; // Output format (mp3, aac, flac, etc.)
  int32 bitrate = 2; // Target bitrate in kbps
  int32 sample_rate = 3; // Target sample rate
  bool normalize_audio = 4; // Normalize audio levels
}
```

---

### extract_audio_response.proto {#extract_audio_response}

**Path**: `gcommon/v1/media/extract_audio_response.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `ExtractAudioResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/extract_audio_response.proto
// version: 1.0.0
// guid: ef01234-5678-9abc-e9f0-a1b2c3d4e5f6

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from audio extraction.
message ExtractAudioResponse {
  string job_id = 1 [(buf.validate.field).string.min_len = 1];
  string status = 2; // pending, processing, completed, failed
  repeated string output_file_ids = 3; // IDs of extracted audio files
  string error_message = 4; // Error details if failed
}
```

---

### extract_subtitles_request.proto {#extract_subtitles_request}

**Path**: `gcommon/v1/media/extract_subtitles_request.proto` **Package**: `gcommon.v1.media` **Lines**: 29

**Messages** (2): `ExtractSubtitlesRequest`, `SubtitleExtractionOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/extract_subtitles_request.proto
// version: 1.0.0
// guid: f012345-6789-abcd-f0a1-b2c3d4e5f6a7

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to extract subtitle tracks from media.
message ExtractSubtitlesRequest {
  string media_file_id = 1 [(buf.validate.field).string.min_len = 1];
  repeated int32 track_indices = 2; // Specific tracks to extract (empty = all)
  SubtitleExtractionOptions options = 3;
}

// Subtitle extraction options.
message SubtitleExtractionOptions {
  string output_format = 1; // Output format (srt, vtt, ass, etc.)
  bool include_hearing_impaired = 2; // Include hearing impaired tracks
  bool include_forced = 3; // Include forced tracks
  repeated string languages = 4; // Filter by languages
}
```

---

### extract_subtitles_response.proto {#extract_subtitles_response}

**Path**: `gcommon/v1/media/extract_subtitles_response.proto` **Package**: `gcommon.v1.media` **Lines**: 33

**Messages** (2): `ExtractSubtitlesResponse`, `ExtractedSubtitle`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/extract_subtitles_response.proto
// version: 1.0.0
// guid: 0123456-789a-bcde-a1b2-c3d4e5f6a7b8

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from subtitle extraction.
message ExtractSubtitlesResponse {
  string job_id = 1 [(buf.validate.field).string.min_len = 1];
  string status = 2; // pending, processing, completed, failed
  repeated ExtractedSubtitle extracted_subtitles = 3 [(buf.validate.field).repeated.min_items = 1];
  string error_message = 4; // Error details if failed
}

// Information about an extracted subtitle file.
message ExtractedSubtitle {
  string file_id = 1 [(buf.validate.field).string.min_len = 1];
  int32 track_index = 2 [(buf.validate.field).int32.gte = 0];
  string language = 3 [(buf.validate.field).string.min_len = 1];
  string title = 4 [(buf.validate.field).string.min_len = 1];
  bool forced = 5;
  bool hearing_impaired = 6;
  string format = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_media_file_request.proto {#get_media_file_request}

**Path**: `gcommon/v1/media/get_media_file_request.proto` **Package**: `gcommon.v1.media` **Lines**: 21

**Messages** (1): `GetMediaFileRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/get_media_file_request.proto
// version: 1.0.0
// guid: 5c6d7e8f-9012-3456-d7e8-f9a0b1c2d3e4

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to get a media file by ID.
message GetMediaFileRequest {
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
}
```

---

### get_media_file_response.proto {#get_media_file_response}

**Path**: `gcommon/v1/media/get_media_file_response.proto` **Package**: `gcommon.v1.media` **Lines**: 18

**Messages** (1): `GetMediaFileResponse`

**Imports** (2):

- `gcommon/v1/media/media_file.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/get_media_file_response.proto
// version: 1.0.1
// guid: 6d7e8f90-1234-5678-e9f0-a1b2c3d4e5f6

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_file.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response containing a media file.
message GetMediaFileResponse {
  MediaFile media_file = 1;
}
```

---

### get_processing_status_request.proto {#get_processing_status_request}

**Path**: `gcommon/v1/media/get_processing_status_request.proto` **Package**: `gcommon.v1.media` **Lines**: 19

**Messages** (1): `GetProcessingStatusRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/get_processing_status_request.proto
// version: 1.0.0
// guid: 1234567-89ab-cdef-b2c3-d4e5f6a7b8c9

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to get processing job status.
message GetProcessingStatusRequest {
  string job_id = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_processing_status_response.proto {#get_processing_status_response}

**Path**: `gcommon/v1/media/get_processing_status_response.proto` **Package**: `gcommon.v1.media` **Lines**: 27

**Messages** (1): `GetProcessingStatusResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/get_processing_status_response.proto
// version: 1.0.0
// guid: 2345678-9abc-def0-c3d4-e5f6a7b8c9d0

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response with processing job status.
message GetProcessingStatusResponse {
  string job_id = 1;
  string status = 2; // pending, processing, completed, failed, cancelled
  string job_type = 3; // transcode, analyze, extract_audio, extract_subtitles
  int32 progress_percent = 4; // Progress percentage (0-100)
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];
  google.protobuf.Timestamp updated_at = 6;
  google.protobuf.Timestamp completed_at = 7;
  string error_message = 8; // Error details if failed
  repeated string output_file_ids = 9; // IDs of output files (when completed)
}
```

---

### list_media_files_request.proto {#list_media_files_request}

**Path**: `gcommon/v1/media/list_media_files_request.proto` **Package**: `gcommon.v1.media` **Lines**: 24

**Messages** (1): `ListMediaFilesRequest`

**Imports** (3):

- `gcommon/v1/common/media_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/list_media_files_request.proto
// version: 1.0.0
// guid: 1234567-89ab-cdef-d6e7-f8a9b0c1d2e3

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/common/media_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to list media files with filtering options.
message ListMediaFilesRequest {
  int32 page_size = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
  string page_token = 2 [(buf.validate.field).string.min_len = 1];
  gcommon.v1.common.MediaType media_type = 3; // Filter by media type
  string path_prefix = 4; // Filter by path prefix
  bool include_metadata = 5; // Include full metadata in response
}
```

---

### list_media_files_response.proto {#list_media_files_response}

**Path**: `gcommon/v1/media/list_media_files_response.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `ListMediaFilesResponse`

**Imports** (3):

- `gcommon/v1/media/media_file.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/list_media_files_response.proto
// version: 1.0.0
// guid: 2345678-9abc-def0-e7f8-a9b0c1d2e3f4

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_file.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response containing a list of media files.
message ListMediaFilesResponse {
  repeated MediaFile media_files = 1 [(buf.validate.field).repeated.min_items = 1];
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### merge_audio_request.proto {#merge_audio_request}

**Path**: `gcommon/v1/media/merge_audio_request.proto` **Package**: `gcommon.v1.media` **Lines**: 19

**Messages** (1): `MergeAudioRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/merge_audio_request.proto
// version: 1.0.0
// guid: 89abcde-f012-3456-a5b6-c7d8e9f0a1b2

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

message MergeAudioRequest {
  repeated string audio_file_ids = 1 [(buf.validate.field).repeated.min_items = 1];
  string output_format = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### merge_audio_response.proto {#merge_audio_response}

**Path**: `gcommon/v1/media/merge_audio_response.proto` **Package**: `gcommon.v1.media` **Lines**: 18

**Messages** (1): `MergeAudioResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/merge_audio_response.proto
// version: 1.0.0
// guid: 9abcdef-0123-4567-b6c7-d8e9f0a1b2c3

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

message MergeAudioResponse {
  string merged_audio_file_id = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### merge_subtitles_request.proto {#merge_subtitles_request}

**Path**: `gcommon/v1/media/merge_subtitles_request.proto` **Package**: `gcommon.v1.media` **Lines**: 20

**Messages** (1): `MergeSubtitlesRequest`

**Imports** (2):

- `gcommon/v1/media/merge_options.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/merge_subtitles_request.proto
// version: 1.0.1
// guid: 123456ab-cdef-0123-f6a7-b8c9d0e1f234

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/merge_options.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to merge multiple subtitle files.
message MergeSubtitlesRequest {
  repeated string subtitle_file_ids = 1; // IDs of subtitle files to merge
  string output_file_id = 2; // Optional output file ID
  MergeOptions merge_options = 3; // Merge configuration options
}
```

---

### merge_subtitles_response.proto {#merge_subtitles_response}

**Path**: `gcommon/v1/media/merge_subtitles_response.proto` **Package**: `gcommon.v1.media` **Lines**: 21

**Messages** (1): `MergeSubtitlesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/merge_subtitles_response.proto
// version: 1.0.0
// guid: 567890ab-cdef-0123-f6a7-b8c9d0e1f234

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from merging subtitle files.
message MergeSubtitlesResponse {
  string merged_subtitle_file_id = 1 [(buf.validate.field).string.min_len = 1];
  bool success = 2;
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### normalize_audio_request.proto {#normalize_audio_request}

**Path**: `gcommon/v1/media/normalize_audio_request.proto` **Package**: `gcommon.v1.media` **Lines**: 27

**Messages** (2): `NormalizeAudioRequest`, `NormalizationOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/normalize_audio_request.proto
// version: 1.0.0
// guid: 456789a-bcde-f012-c1d2-e3f4a5b6c7d8

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to normalize audio levels.
message NormalizeAudioRequest {
  string audio_file_id = 1 [(buf.validate.field).string.min_len = 1];
  NormalizationOptions options = 2;
}

// Audio normalization options.
message NormalizationOptions {
  double target_lufs = 1; // Target loudness in LUFS (-23.0 is broadcast standard)
  double max_peak_db = 2; // Maximum peak level in dB
  bool enable_limiter = 3; // Enable limiting to prevent clipping
}
```

---

### normalize_audio_response.proto {#normalize_audio_response}

**Path**: `gcommon/v1/media/normalize_audio_response.proto` **Package**: `gcommon.v1.media` **Lines**: 23

**Messages** (1): `NormalizeAudioResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/normalize_audio_response.proto
// version: 1.0.0
// guid: 56789ab-cdef-0123-d2e3-f4a5b6c7d8e9

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from audio normalization.
message NormalizeAudioResponse {
  string normalized_audio_file_id = 1 [(buf.validate.field).string.min_len = 1];
  double original_lufs = 2; // Original loudness level
  double normalized_lufs = 3; // Resulting loudness level
  double gain_applied_db = 4; // Gain adjustment applied
  bool limiting_applied = 5; // Whether limiting was applied
}
```

---

### search_media_request.proto {#search_media_request}

**Path**: `gcommon/v1/media/search_media_request.proto` **Package**: `gcommon.v1.media` **Lines**: 25

**Messages** (1): `SearchMediaRequest`

**Imports** (3):

- `gcommon/v1/common/media_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/search_media_request.proto
// version: 1.0.0
// guid: 3456789-abcd-ef01-f8a9-b0c1d2e3f4a5

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/common/media_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to search media files.
message SearchMediaRequest {
  string query = 1; // Search query string
  gcommon.v1.common.MediaType media_type = 2; // Filter by media type
  repeated string tags = 3; // Search by tags
  string language = 4; // Filter by language
  int32 page_size = 5 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
  string page_token = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### search_media_response.proto {#search_media_response}

**Path**: `gcommon/v1/media/search_media_response.proto` **Package**: `gcommon.v1.media` **Lines**: 23

**Messages** (1): `SearchMediaResponse`

**Imports** (3):

- `gcommon/v1/media/media_file.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/search_media_response.proto
// version: 1.0.0
// guid: 456789a-bcde-f012-a9b0-c1d2e3f4a5b6

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_file.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response containing search results.
message SearchMediaResponse {
  repeated MediaFile media_files = 1 [(buf.validate.field).repeated.min_items = 1];
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];
  repeated string suggested_terms = 4; // Search suggestions
}
```

---

### split_audio_request.proto {#split_audio_request}

**Path**: `gcommon/v1/media/split_audio_request.proto` **Package**: `gcommon.v1.media` **Lines**: 27

**Messages** (2): `SplitAudioRequest`, `SplitPoint`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/split_audio_request.proto
// version: 1.0.0
// guid: 6789abc-def0-1234-e3f4-a5b6c7d8e9f0

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

message SplitAudioRequest {
  string audio_file_id = 1;
  repeated SplitPoint split_points = 2;
}

message SplitPoint {
  google.protobuf.Duration timestamp = 1;
  string segment_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
}
```

---

### split_audio_response.proto {#split_audio_response}

**Path**: `gcommon/v1/media/split_audio_response.proto` **Package**: `gcommon.v1.media` **Lines**: 18

**Messages** (1): `SplitAudioResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/split_audio_response.proto
// version: 1.0.0
// guid: 789abcd-ef01-2345-f4a5-b6c7d8e9f0a1

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

message SplitAudioResponse {
  repeated string segment_file_ids = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### sync_subtitles_request.proto {#sync_subtitles_request}

**Path**: `gcommon/v1/media/sync_subtitles_request.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `SyncSubtitlesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/sync_subtitles_request.proto
// version: 1.0.0
// guid: 012345f0-1234-5678-e1f2-345678901234

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to synchronize subtitles with media.
message SyncSubtitlesRequest {
  string subtitle_file_id = 1 [(buf.validate.field).string.min_len = 1];
  string media_file_id = 2 [(buf.validate.field).string.min_len = 1];
  bool auto_detect_timing = 3; // Whether to automatically detect timing
  repeated int64 sync_points_ms = 4; // Manual sync points in milliseconds
}
```

---

### sync_subtitles_response.proto {#sync_subtitles_response}

**Path**: `gcommon/v1/media/sync_subtitles_response.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `SyncSubtitlesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/sync_subtitles_response.proto
// version: 1.0.0
// guid: 234567bc-def0-1234-f6a7-b8c9d0e1f234

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from synchronizing subtitles with media.
message SyncSubtitlesResponse {
  string synchronized_subtitle_file_id = 1 [(buf.validate.field).string.min_len = 1];
  bool success = 2;
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
  int32 adjustments_made = 4; // Number of timing adjustments made
}
```

---

### transcode_media_request.proto {#transcode_media_request}

**Path**: `gcommon/v1/media/transcode_media_request.proto` **Package**: `gcommon.v1.media` **Lines**: 23

**Messages** (1): `TranscodeMediaRequest`

**Imports** (3):

- `gcommon/v1/media/transcode_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/transcode_media_request.proto
// version: 1.0.0
// guid: 89abcde-f012-3456-e3f4-a5b6c7d8e9f0

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/transcode_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to transcode media to different format.
message TranscodeMediaRequest {
  string media_file_id = 1 [(buf.validate.field).string.min_len = 1];
  string output_format = 2; // Target format (mp4, mkv, avi, etc.)
  string output_codec = 3; // Target codec (h264, h265, av1, etc.)
  TranscodeOptions options = 4;
}
```

---

### transcode_media_response.proto {#transcode_media_response}

**Path**: `gcommon/v1/media/transcode_media_response.proto` **Package**: `gcommon.v1.media` **Lines**: 23

**Messages** (1): `TranscodeMediaResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/transcode_media_response.proto
// version: 1.0.0
// guid: 9abcdef-0123-4567-f4a5-b6c7d8e9f0a1

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from transcoding request.
message TranscodeMediaResponse {
  string job_id = 1 [(buf.validate.field).string.min_len = 1];
  string status = 2; // pending, processing, completed, failed
  string output_file_id = 3; // ID of the transcoded file (when completed)
  int32 progress_percent = 4; // Progress percentage (0-100)
  string error_message = 5; // Error details if failed
}
```

---

### update_media_file_request.proto {#update_media_file_request}

**Path**: `gcommon/v1/media/update_media_file_request.proto` **Package**: `gcommon.v1.media` **Lines**: 20

**Messages** (1): `UpdateMediaFileRequest`

**Imports** (3):

- `gcommon/v1/media/media_file.proto`
- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/update_media_file_request.proto
// version: 1.0.1
// guid: 7e8f9012-3456-7890-f1a2-b3c4d5e6f7a8

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_file.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to update a media file.
message UpdateMediaFileRequest {
  MediaFile media_file = 1;
  google.protobuf.FieldMask update_mask = 2;
}
```

---

### update_media_file_response.proto {#update_media_file_response}

**Path**: `gcommon/v1/media/update_media_file_response.proto` **Package**: `gcommon.v1.media` **Lines**: 18

**Messages** (1): `UpdateMediaFileResponse`

**Imports** (2):

- `gcommon/v1/media/media_file.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/update_media_file_response.proto
// version: 1.0.1
// guid: 8f901234-5678-9012-a3b4-c5d6e7f8a9b0

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_file.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from updating a media file.
message UpdateMediaFileResponse {
  MediaFile media_file = 1;
}
```

---

### upload_media_request.proto {#upload_media_request}

**Path**: `gcommon/v1/media/upload_media_request.proto` **Package**: `gcommon.v1.media` **Lines**: 31

**Messages** (2): `UploadMediaRequest`, `UploadMetadata`

**Imports** (3):

- `gcommon/v1/media/media_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/upload_media_request.proto
// version: 1.0.0
// guid: 56789ab-cdef-0123-b0c1-d2e3f4a5b6c7

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to upload media content (streaming).
message UploadMediaRequest {
  oneof data {
    UploadMetadata metadata = 1;
    bytes chunk = 2;
  }
}

// Metadata for media upload.
message UploadMetadata {
  string filename = 1 [(buf.validate.field).string.min_len = 1];
  string content_type = 2 [(buf.validate.field).string.min_len = 1];
  int64 total_size = 3 [(buf.validate.field).int64.gte = 0];
  MediaMetadata media_metadata = 4;
}
```

---

### upload_media_response.proto {#upload_media_response}

**Path**: `gcommon/v1/media/upload_media_response.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `UploadMediaResponse`

**Imports** (3):

- `gcommon/v1/media/media_file.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/upload_media_response.proto
// version: 1.0.0
// guid: 6789abc-def0-1234-c1d2-e3f4a5b6c7d8

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/media_file.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from uploading media.
message UploadMediaResponse {
  MediaFile media_file = 1;
  string upload_id = 2 [(buf.validate.field).string.min_len = 1];
  bool success = 3;
}
```

---

### validate_subtitles_request.proto {#validate_subtitles_request}

**Path**: `gcommon/v1/media/validate_subtitles_request.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `ValidateSubtitlesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/validate_subtitles_request.proto
// version: 1.0.0
// guid: 456789de-f012-3456-f6a7-b8c9d0e1f234

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Request to validate subtitle file format and content.
message ValidateSubtitlesRequest {
  string subtitle_file_id = 1 [(buf.validate.field).string.min_len = 1];
  bool check_timing = 2; // Whether to validate timing information
  bool check_formatting = 3; // Whether to validate format compliance
  string expected_format = 4; // Expected subtitle format (srt, vtt, ass, etc.)
}
```

---

### validate_subtitles_response.proto {#validate_subtitles_response}

**Path**: `gcommon/v1/media/validate_subtitles_response.proto` **Package**: `gcommon.v1.media` **Lines**: 20

**Messages** (1): `ValidateSubtitlesResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/validate_subtitles_response.proto
// version: 1.0.1
// guid: 567890ef-0123-4567-f6a7-b8c9d0e1f234

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

// Response from validating subtitle file.
message ValidateSubtitlesResponse {
  bool is_valid = 1;
  repeated string validation_errors = 2; // List of validation errors found
  repeated string validation_warnings = 3; // List of validation warnings
  string detected_format = 4; // Actually detected subtitle format
}
```

---

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

