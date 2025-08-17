<!-- file: examples/modules/queue/worker-pool/README.md -->
<!-- version: 1.1.0 -->
<!-- guid: a795cc9a-a669-44d8-8783-6bc62f9520cc -->

# Worker Pool Example

Demonstrates processing messages concurrently using multiple goroutines. Messages are published to an in-memory queue and workers consume them in parallel.

## Run

```bash
go run .
```

You should see output similar to:

```
worker 0 processed job-0
worker 1 processed job-1
...
```
