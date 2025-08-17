# Proto File Splitting Guide - 1-1-1 Pattern Implementation

## Progress Summary

### ✅ Completed Files - ALL DONE

**Manual Splits Completed:**

- `stats_granularity.proto` - Already following 1-1-1 pattern (1 enum only)
- `alerting_config.proto` - Split into 6 files (3 enums + 3 messages)
- `nack_request.proto` - Split into 3 files (1 enum + 2 messages)
- `load_balancing_config.proto` - Split into 2 files (1 enum + 1 message)

**Automated Splits Completed (using split_proto.py):**

- `serialization_config.proto` - Split into 3 files
- `delete_provider_request.proto` - Split into 3 files
- `record_metrics_request.proto` - Split into 3 files
- `get_queue_stats_request.proto` - Split into 3 files
- `replication_config.proto` - Split into 3 files
- `schema_config.proto` - Split into 4 files
- `config_audit_log.proto` - Split into 4 files
- `config_restore_point.proto` - Split into 4 files
- `update_provider_response.proto` - Split into 5 files
- `cluster_info.proto` - Split into 7 files
- `routing_config.proto` - Split into 8 files
- `config_version.proto` - Split into 13 files
- `config_template.proto` - Split into 13 files
- `update_provider_request.proto` - Split into 15 files
- `config_metadata.proto` - Split into 16 files
- `config_secret.proto` - Split into 26 files
- `config_value.proto` - Split into 35 files

**Total Result:** 16 large files split into ~180+ individual files, all following the 1-1-1 pattern.

## Standard Splitting Process

### For Each File

1. **Backup**: `cp original.proto original.proto.backup.$(date +%Y%m%d_%H%M%S)`

2. **Extract Enums**: For each enum, create `enum_name.proto`:

   ```proto3
   // file: pkg/path/proto/enum_name.proto
   // version: 1.0.0
   // guid: [new-guid]

   edition = "2023";
   package gcommon.v1.[module];
   import "google/protobuf/go_features.proto";
   option features.(pb.go).api_level = API_OPAQUE;
   option go_package = "github.com/jdfalk/gcommon/pkg/[module]/proto;[module]pb";

   enum EnumName {
     // definitions...
   }
   ```

3. **Extract Messages**: For each message, create `message_name.proto`:

   ```proto3
   // file: pkg/path/proto/message_name.proto
   // version: 1.0.0
   // guid: [new-guid]

   edition = "2023";
   package gcommon.v1.[module];
   import "google/protobuf/go_features.proto";
   import "pkg/[module]/proto/required_enum.proto";
   option features.(pb.go).api_level = API_OPAQUE;
   option go_package = "github.com/jdfalk/gcommon/pkg/[module]/proto;[module]pb";

   message MessageName {
     // definitions...
   }
   ```

4. **Update Original**: Rename and update original file to import dependencies

5. **Test**: Check for compilation errors

## Naming Conventions

### File Names

- Enums: `snake_case.proto` (e.g., `load_balancing_strategy.proto`)
- Messages: `snake_case.proto` (e.g., `nack_request.proto`)

### Import Statements

- Always import the specific files needed
- Use relative paths: `pkg/[module]/proto/file_name.proto`

## Benefits of 1-1-1 Pattern

1. **Modularity**: Each file has a single responsibility
2. **Reusability**: Enums can be imported independently
3. **Maintainability**: Easier to locate and modify specific definitions
4. **Build Efficiency**: Only recompile what changed
5. **Clarity**: Clear file structure and dependencies

## Tools Created

1. `analyze_proto_files.sh` - Analyze all files that need splitting
2. `split_proto.py` - Automated splitting script that successfully split all files

## Usage

To split a protobuf file:

```bash
python3 split_proto.py path/to/file.proto
```

To analyze current status:

```bash
./analyze_proto_files.sh
```

## Validation

After splitting, verify:

- [ ] All original definitions are preserved
- [ ] Import statements are correct
- [ ] No compilation errors
- [ ] File follows naming conventions
- [ ] GUID is unique for each new file
