<!-- file: examples/modules/queue/job-scheduler/README.md -->
<!-- version: 1.1.0 -->
<!-- guid: 63faf064-81eb-466b-812b-c28bff33e628 -->

# Job Scheduler Example

Uses the `jobs.Scheduler` to execute a task in the future. A job is scheduled to run one second after startup and prints a message when executed.

## Run

```bash
go run .
```

The program waits briefly for the job to complete and then outputs the job's completion status.
