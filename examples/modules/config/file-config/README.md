<!-- file: examples/modules/config/file-config/README.md -->
<!-- version: 1.1.0 -->
<!-- guid: 737a2a6b-5333-4a6d-ae2c-400a2e3f5a09 -->

# File Config Example

Demonstrates loading configuration from a YAML file using gcommon's loader. Defaults defined in code are merged with file values.

## Sample `config.yaml`

```yaml
timeout: 10
```

## Run

```bash
go run .
```

The program prints the merged configuration showing that values from the file override defaults.
