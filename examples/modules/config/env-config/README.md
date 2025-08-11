<!-- file: examples/modules/config/env-config/README.md -->
<!-- version: 1.1.0 -->
<!-- guid: cd76db96-f4d4-4101-89f5-054aaebe2e26 -->

# Env Config Example

Loads configuration from environment variables using the `EnvSource`. Variables
must be prefixed with `APP_` to be recognized.

## Run

```bash
export APP_GREETING=world
go run .
```

The output shows a map containing `{"GREETING": "world"}`.

## Related Examples

- [Basic Config](../basic-config/README.md)
- [Dynamic Config](../dynamic-config/README.md)
