<!-- file: examples/getting-started/basic-setup/README.md -->
<!-- version: 1.1.0 -->
<!-- guid: 92d02bc5-e8b2-4591-847f-9e228ae9ccd9 -->

# Basic Setup Example

This example demonstrates the smallest possible program that uses gcommon. It
loads configuration from a YAML file and prints the resulting map to standard
output.

## Prerequisites

- Go 1.23 or later
- A `config.yaml` file in the same directory (a sample is shown below)

```yaml
app:
  name: demo
  port: 8080
```

## Running the Example

```bash
go run .
```

The program loads the configuration and prints the merged settings. Additional
sources such as environment variables can be added by extending the loader in
`main.go`.

## Next Steps

- Explore other examples in this repository
- Read the configuration module documentation for advanced scenarios
