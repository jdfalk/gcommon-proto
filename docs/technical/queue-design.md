# Queue Module Technical Design

## Overview

The queue module provides a unified interface for message queuing and processing with support for multiple queue backends, delivery guarantees, and processing patterns. This design document outlines the architecture, interfaces, and
implementation details for the queue module.

## Goals

- Provide a consistent API for message queuing across applications
- Support multiple queue backends (in-memory, Redis, RabbitMQ, etc.)
- Enable reliable message delivery with acknowledgments
- Support multiple consumption patterns (push/pull, competing consumers)
- Allow for message prioritization and scheduling
- Enable dead letter queues for failed messages
- Support batch operations for efficiency
- Provide queue management and monitoring
- Enable cross-language message compatibility
- Support message filtering and routing

## Architecture

### Core Components

```plaintext
              +----------------+
   |                  |                   |
+--+------+    +------+------+     +------+------+
| Queues  |    | Consumers   |     | Publishers  |
+---------+    +-------------+     +-------------+
   |                  |                   |
   |                  |                   |
+--+------+    +------+------+     +------+------+
| Memory/ |    | Push/Pull/  |     | Batch/      |
| Redis/  |    | Competing   |     | Single      |
| etc     |    | Consumers   |     | Messages    |
+---------+    +-------------+     +-------------+
```

### Component Design

#### Queue Interface

The core of the module is the `Queue` interface, which defines the common operations for queue management.

```go
type Queue interface {
    // Basic operations
    Publish(ctx context.Context, message *Message) error
    Subscribe(ctx context.Context, config *ConsumerConfig) (<-chan *Message, error)

    // Batch operations
    PublishBatch(ctx context.Context, messages []*Message) error

    // Management operations
    GetInfo(ctx context.Context) (*QueueInfo, error)
    GetStats(ctx context.Context) (*QueueStats, error)
    Purge(ctx context.Context, filter *MessageFilter) error

    // Lifecycle
    Close() error
}
```

#### Message Structure

Messages contain the payload, headers, and metadata:

```go
type Message struct {
    ID          string
    Body        []byte
    Headers     map[string]string
    Priority    int32
    DelayUntil  time.Time
    Attempts    int32
    CreatedAt   time.Time
    DeliveryTag string
}
```

#### Consumer Configuration

Consumers can be configured for different consumption patterns:

```go
type ConsumerConfig struct {
    Name            string
    Concurrency     int
    AckMode         AckMode
    RetryPolicy     *RetryPolicy
    DeadLetterQueue string
    Filter          *MessageFilter
}
```

## Implementation Patterns

### Provider Pattern

Different queue backends implement the `Provider` interface:

- **Memory**: In-process memory queue for testing and simple use cases
- **Redis**: Redis-based distributed queue with persistence
- **RabbitMQ**: Full-featured message broker integration
- **AWS SQS**: Cloud-native queue service
- **Google Pub/Sub**: Cloud messaging service

### Acknowledgment Modes

- **Auto**: Messages are automatically acknowledged on delivery
- **Manual**: Consumer must explicitly acknowledge messages
- **Duplicate**: Messages may be delivered multiple times

### Delivery Guarantees

- **At Most Once**: Messages may be lost but never duplicated
- **At Least Once**: Messages may be duplicated but never lost
- **Exactly Once**: Messages are delivered exactly once (when supported)

## Configuration

### Queue Configuration

```yaml
queue:
  provider: 'redis'
  connection: 'redis://localhost:6379'
  queues:
    - name: 'tasks'
      durable: true
      max_length: 10000
      dead_letter_queue: 'tasks_dlq'
    - name: 'events'
      durable: false
      ttl: '1h'
```

### Consumer Configuration

```yaml
consumers:
  - name: 'task_processor'
    queue: 'tasks'
    concurrency: 5
    ack_mode: 'manual'
    retry_policy:
      max_attempts: 3
      backoff: 'exponential'
      initial_delay: '1s'
      max_delay: '5m'
```

## Error Handling

### Retry Policies

- **Linear Backoff**: Fixed delay between retries
- **Exponential Backoff**: Exponentially increasing delays
- **Custom**: User-defined retry logic

### Dead Letter Queues

Failed messages are sent to dead letter queues after exhausting retries, allowing for:

- Manual inspection and reprocessing
- Alerting on failed messages
- Analysis of failure patterns

## Monitoring and Metrics

### Key Metrics

- **Queue Depth**: Number of pending messages
- **Throughput**: Messages per second (publish/consume)
- **Latency**: Time from publish to consume
- **Error Rate**: Failed message percentage
- **Consumer Health**: Active consumer count and status

### Health Checks

- Queue connectivity
- Consumer responsiveness
- Dead letter queue growth
- Memory/storage usage

## Security

### Authentication

- Connection-level authentication (Redis AUTH, AMQP credentials)
- Message-level authentication headers
- Client certificate validation

### Authorization

- Queue-level access controls
- Operation-specific permissions (publish vs. consume)
- Message filtering based on permissions

## Performance Considerations

### Optimization Techniques

- **Connection Pooling**: Reuse connections across operations
- **Batch Processing**: Group operations for efficiency
- **Prefetching**: Consumer-side message buffering
- **Compression**: Compress large message payloads

### Scalability

- **Horizontal Scaling**: Multiple queue instances
- **Partitioning**: Distribute messages across partitions
- **Load Balancing**: Distribute consumers across instances

## Integration

### Health Module Integration

- Queue health checks
- Consumer health monitoring
- Automatic remediation for failed consumers

### Metrics Module Integration

- Queue metrics collection
- Consumer performance metrics
- Business metrics extraction from messages

### Logging Module Integration

- Message publish/consume logging
- Error and retry logging
- Audit trails for message processing

## Usage Examples

### Basic Publisher

```go
provider := queue.NewRedisProvider(config)
q, err := provider.GetQueue("tasks")
if err != nil {
    log.Fatal(err)
}

message := &queue.Message{
    Body: []byte("task payload"),
    Headers: map[string]string{
        "type": "user_notification",
        "priority": "high",
    },
}

err = q.Publish(ctx, message)
if err != nil {
    log.Error("Failed to publish message", err)
}
```

### Basic Consumer

```go
config := &queue.ConsumerConfig{
    Name:        "notification_processor",
    Concurrency: 3,
    AckMode:     queue.ManualAck,
}

messages, err := q.Subscribe(ctx, config)
if err != nil {
    log.Fatal(err)
}

for message := range messages {
    err := processMessage(message)
    if err != nil {
        message.Reject(true) // Requeue
    } else {
        message.Ack() // Acknowledge
    }
}
```

## Testing Strategy

### Unit Tests

- Provider interface compliance
- Message serialization/deserialization
- Consumer configuration validation
- Retry logic testing

### Integration Tests

- End-to-end message flow
- Multiple consumer coordination
- Dead letter queue behavior
- Provider-specific features

### Performance Tests

- Throughput benchmarks
- Latency measurements
- Resource usage profiling
- Scalability testing

## Migration and Deployment

### Zero-Downtime Deployment

- Blue-green deployment of consumers
- Message draining strategies
- Rolling updates with consumer coordination

### Data Migration

- Queue content migration between providers
- Message format evolution
- Dead letter queue cleanup

This queue module design provides a robust foundation for message queuing across diverse applications while maintaining consistency with the overall GCommon architecture.
