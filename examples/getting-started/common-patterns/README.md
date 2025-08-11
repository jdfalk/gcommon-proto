<!-- file: examples/getting-started/common-patterns/README.md -->
<!-- version: 1.1.0 -->
<!-- guid: 03cb484b-3610-45e6-ae96-0737e532e4c3 -->

# Common Patterns Example

This example illustrates how configuration, metrics, and queue components can be
combined in a small application. It loads settings from environment variables,
publishes a message to a queue, and tracks processing with a counter metric.

## Highlights

- Environment-based configuration loading
- In-memory queue for message passing
- Prometheus metrics provider for instrumentation

## Running

```bash
go run .
```

## Environment Variables

Set the following variables to see configuration merging in action:

```bash
export APP_PORT=9000
export APP_ENV=development
```

The loaded configuration is printed to the console.
