# Protovalidate Integration for gcommon Repository

This document provides comprehensive guidance for implementing and using protovalidate validation rules in the gcommon repository's 1600+ protobuf files.

## Overview

The protovalidate integration system provides automated tools for adding validation rules to protobuf fields based on intelligent semantic analysis. This ensures data integrity, improves API reliability, and provides better error messages for invalid input.

## Architecture

### Core Components

1. **`tools/protovalidate-adder.py`** - Main automation tool for processing proto files
2. **`scripts/add-protovalidate.sh`** - User-friendly wrapper script with command-line interface  
3. **VS Code Tasks** - Integrated development workflow support
4. **Example Files** - Sample implementations demonstrating validation patterns

### Dependencies

- **buf.yaml**: Includes `buf.build/bufbuild/protovalidate` dependency
- **buf.gen.yaml**: Configured with protovalidate-go plugin for code generation
- **Python 3.7+**: Required for the automation tool

## Installation and Setup

### Prerequisites

Ensure the following are available in your environment:

```bash
# Check Python availability
python3 --version  # Should be 3.7 or higher

# Verify buf configuration
cat buf.yaml  # Should include protovalidate dependency
```

### Verification

The repository is already configured with protovalidate dependencies. Verify the setup:

```bash
# Check buf.yaml includes protovalidate
grep -A 10 "deps:" buf.yaml

# Check buf.gen.yaml includes protovalidate-go plugin  
grep -A 5 "protovalidate-go" buf.gen.yaml

# Verify tools are executable
ls -la tools/protovalidate-adder.py
ls -la scripts/add-protovalidate.sh
```

## Usage Guide

### Quick Start

```bash
# Process all proto files (with confirmation prompt)
./scripts/add-protovalidate.sh --all

# Preview changes without modification (recommended first step)
./scripts/add-protovalidate.sh --dry-run

# Process specific file
./scripts/add-protovalidate.sh --file proto/gcommon/v1/auth/user.proto

# Use compatibility mode for gradual adoption
./scripts/add-protovalidate.sh --compatibility --all
```

### Direct Python Tool Usage

```bash
# Process all files
python3 tools/protovalidate-adder.py

# Dry run mode
python3 tools/protovalidate-adder.py --dry-run

# Process specific file
python3 tools/protovalidate-adder.py --file proto/gcommon/v1/auth/user.proto

# Compatibility mode
python3 tools/protovalidate-adder.py --compatibility-mode

# Verbose output
python3 tools/protovalidate-adder.py --verbose
```

### VS Code Integration

Use the integrated VS Code tasks for seamless development workflow:

1. **Add Protovalidate - All Files**: Process entire repository
2. **Add Protovalidate - Dry Run**: Preview changes without modification  
3. **Add Protovalidate - Compatibility Mode**: Add rules as comments
4. **Add Protovalidate - Specific File**: Process individual files
5. **Add Protovalidate - Using Wrapper Script**: Use the shell wrapper

Access via: Command Palette → "Tasks: Run Task" → Select protovalidate task

## Validation Rule Patterns

The tool automatically generates appropriate validation rules based on field semantics:

### Field Pattern Recognition

| Field Pattern | Applied Rule | Example Fields |
|--------------|--------------|----------------|
| `*_id`, `id` | `string.min_len = 1` | `user_id`, `client_id` |
| `*email*` | Email regex pattern | `email`, `contact_email` |
| `*age*` | `int32.gte = 0, int32.lte = 150` | `age`, `user_age` |
| `*url*`, `*uri*` | `string.uri = true` | `api_url`, `profile_url` |
| `*port*` | `int32.gte = 1, int32.lte = 65535` | `port`, `server_port` |
| `*percent*` | `float.gte = 0.0, float.lte = 100.0` | `percentage`, `completion` |
| `*phone*` | Phone number regex | `phone`, `mobile_phone` |
| `*name*`, `*title*` | `string.min_len = 1` | `name`, `display_name` |
| `*password*` | `string.min_len = 8` | `password`, `user_password` |
| `*token*` | `string.min_len = 1` | `token`, `api_token` |
| `*version*` | Semantic version regex | `version`, `api_version` |
| `*count*`, `*size*` | `int32.gte = 0` | `count`, `file_size` |
| `*timeout*`, `*duration*` | `int32.gt = 0` | `timeout`, `session_duration` |
| `*code*` | `string.min_len = 1` | `code`, `tfa_code` |
| `repeated` fields | `repeated.min_items = 1` | All repeated fields |

### Default Type Rules

For fields not matching specific patterns:

| Type | Default Rule |
|------|-------------|
| `string` | `string.min_len = 1` |
| `int32` | `int32.gte = 0` |
| `int64` | `int64.gte = 0` |
| `uint32` | `uint32.gte = 0` |
| `uint64` | `uint64.gte = 0` |
| `float` | `float.gte = 0.0` |
| `double` | `double.gte = 0.0` |
| `repeated` | `repeated.min_items = 1` |

### Skipped Field Patterns

The tool intelligently skips fields that are typically optional or complex:

- `*metadata*` - Configuration/metadata maps
- `*timestamp*` - Timestamp fields  
- `*any*` - google.protobuf.Any fields

## Examples

### Basic Field Validation

```protobuf
// Before processing
message UserInfo {
  string user_id = 1;
  string email = 2;
  int32 age = 3;
  repeated string roles = 4;
}

// After processing
message UserInfo {
  string user_id = 1 [(validate.rules).string.min_len = 1];
  string email = 2 [(validate.rules).string.pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"];
  int32 age = 3 [(validate.rules).int32.gte = 0, (validate.rules).int32.lte = 150];
  repeated string roles = 4 [(validate.rules).repeated.min_items = 1];
}
```

### Import Addition

The tool automatically adds the required import:

```protobuf
// Added automatically
import "buf/validate/validate.proto";
```

### Compatibility Mode

In environments where protovalidate is not yet available:

```protobuf
// Compatibility mode output
message UserInfo {
  string user_id = 1;  // Validation: [(validate.rules).string.min_len = 1]
  string email = 2;    // Validation: [(validate.rules).string.pattern = "..."]
}
```

## Operational Modes

### 1. Standard Mode (Default)

- Adds protovalidate import
- Applies validation rules directly to fields
- Modifies files in-place

### 2. Dry Run Mode

- Shows what changes would be made
- No files are modified
- Useful for previewing changes before applying

### 3. Compatibility Mode

- Adds validation rules as comments
- No import statements added
- Enables gradual migration approach

## Integration with Existing Workflow

### Build Integration

After adding validation rules, regenerate code:

```bash
# Using Makefile
make generate

# Or directly with buf
buf generate
```

### Git Workflow

Recommended workflow for large-scale changes:

```bash
# 1. Preview changes
./scripts/add-protovalidate.sh --dry-run

# 2. Apply to subset first (optional)
./scripts/add-protovalidate.sh --file proto/gcommon/v1/auth/user.proto

# 3. Test build
make generate

# 4. Apply to all files
./scripts/add-protovalidate.sh --all

# 5. Verify and commit
git add .
git commit -m "feat(proto): add protovalidate validation rules"
```

### Code Generation

The buf.gen.yaml is configured to generate Go validation code:

```yaml
- plugin: buf.build/bufbuild/protovalidate-go:v0.6.3
  out: sdks/go
  strategy: directory
  opt:
    - paths=import
    - module=github.com/jdfalk/gcommon/sdks/go
```

## Performance Considerations

### Large-Scale Processing

The tool is optimized for processing thousands of files:

- **Memory efficient**: Processes files one at a time
- **Fast pattern matching**: Uses compiled regex patterns
- **Error resilient**: Continues processing if individual files fail
- **Progress reporting**: Provides detailed logging and statistics

### Processing Statistics

For a repository with 1600+ files, expect:

- **Processing time**: 2-5 minutes depending on system
- **Memory usage**: <100MB typical
- **Disk I/O**: Minimal (only modified files are written)

## Troubleshooting

### Common Issues

**1. Import already exists error**
```
Solution: Tool automatically detects existing imports
```

**2. Validation rules already present**
```
Solution: Tool preserves existing rules by default
```

**3. Python not found**
```bash
# Ensure Python 3.7+ is available
python3 --version
```

**4. Permission denied**
```bash
# Make scripts executable
chmod +x tools/protovalidate-adder.py
chmod +x scripts/add-protovalidate.sh
```

### Debug Mode

Enable verbose logging for troubleshooting:

```bash
python3 tools/protovalidate-adder.py --verbose --dry-run
```

### Validation

Verify the results after processing:

```bash
# Check for validation imports
grep -r "buf/validate/validate.proto" proto/

# Check for validation rules
grep -r "validate.rules" proto/ | head -10

# Test build
make generate
```

## Advanced Usage

### Custom Field Patterns

The tool's pattern recognition can be extended by modifying the `field_patterns` dictionary in `protovalidate-adder.py`:

```python
# Add custom pattern
self.field_patterns[r'.*custom_field.*'] = {
    'string': '[(validate.rules).string.custom_rule = true]'
}
```

### Selective Processing

Process specific modules:

```bash
# Process only auth module
find proto/gcommon/v1/auth -name "*.proto" -exec python3 tools/protovalidate-adder.py --file {} \;

# Process only specific patterns
find proto -name "*_request.proto" -exec python3 tools/protovalidate-adder.py --file {} \;
```

### Integration with CI/CD

Add validation checks to CI pipeline:

```yaml
# .github/workflows/validate-proto.yml
- name: Validate protovalidate rules
  run: |
    python3 tools/protovalidate-adder.py --dry-run
    if [ $? -ne 0 ]; then
      echo "Protovalidate rules need to be added"
      exit 1
    fi
```

## Best Practices

### Field Naming

To maximize validation rule effectiveness:

- Use semantic field names: `user_email` vs `field1`
- Follow consistent naming patterns: `*_url`, `*_count`, `*_duration`
- Use descriptive field names that indicate their purpose

### Gradual Adoption

For large repositories:

1. Start with compatibility mode
2. Process critical modules first
3. Test with small subsets
4. Gradually expand coverage
5. Monitor build and runtime performance

### Code Reviews

When reviewing protovalidate changes:

- Verify validation rules match field semantics
- Check for appropriate constraint ranges
- Ensure imports are correctly added
- Test with invalid data to verify enforcement

## Monitoring and Maintenance

### Validation Coverage

Track validation coverage across modules:

```bash
# Count total proto files
find proto -name "*.proto" | wc -l

# Count files with validation rules
grep -l "validate.rules" proto/**/*.proto | wc -l

# Generate coverage report
python3 tools/protovalidate-adder.py --dry-run | grep "would modify" | wc -l
```

### Regular Updates

Maintain the validation rules:

- Review new field patterns in code reviews
- Update validation rules when business logic changes
- Monitor for new protovalidate features and constraints

## Migration Guide

### From Manual Validation

If you have existing manual validation:

1. Run tool in dry-run mode to see proposed changes
2. Compare with existing validation logic
3. Update custom validation to use protovalidate
4. Remove redundant manual validation code

### Version Compatibility

- **Protovalidate**: Compatible with v0.6.3+
- **Protobuf**: Requires Edition 2023 support
- **Go**: Generated code requires Go 1.19+
- **Python**: Tool requires Python 3.7+

## Resources

### Documentation

- [Protovalidate Official Docs](https://buf.build/bufbuild/protovalidate)
- [Edition 2023 Guide](https://protobuf.dev/programming-guides/editions/)
- [Buf Configuration](https://buf.build/docs/configuration/v2)

### Support

For issues or questions:

1. Check this documentation
2. Review error messages and logs
3. Use dry-run mode to diagnose issues
4. Check GitHub issues in the gcommon repository

---

**Note**: This integration system is designed to handle the scale and complexity of the gcommon repository with its 1600+ protobuf files. The intelligent pattern recognition and safe processing modes ensure reliable, large-scale validation rule deployment.