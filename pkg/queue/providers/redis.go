// file: pkg/queue/providers/redis.go
// version: 1.1.0
// guid: 17ce4e70-7beb-4eea-9b16-69139474add4

package providers

import (
	"context"
	"fmt"
	"time"

	"github.com/go-redis/redis/v8"
	"github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
	"google.golang.org/protobuf/proto"
)

// RedisQueue implements Queue using Redis lists for storage. Each queue is
// represented as a Redis list with a configurable key prefix. Messages are
// marshaled using protobuf for transport.
type RedisQueue struct {
	client *redis.Client
	prefix string
}

// NewRedisQueue creates a Redis-backed queue provider. The addr parameter is
// passed directly to the underlying redis client. The prefix parameter is
// prepended to all Redis keys; if empty, "queue:" is used.
func NewRedisQueue(addr, prefix string) (*RedisQueue, error) {
	if prefix == "" {
		prefix = "queue:"
	}
	r := &RedisQueue{
		client: redis.NewClient(&redis.Options{Addr: addr}),
		prefix: prefix,
	}
	if err := r.client.Ping(context.Background()).Err(); err != nil {
		return nil, err
	}
	return r, nil
}

// key returns the redis key for a queue name.
func (r *RedisQueue) key(name string) string { return r.prefix + name }

// Publish enqueues a message into the Redis list associated with the queue
// identified in the context. Messages are marshaled using protobuf.
func (r *RedisQueue) Publish(ctx context.Context, message *queuepb.QueueMessage) error {
	name, ok := queue.QueueNameFromContext(ctx)
	if !ok {
		name = "default"
	}
	data, err := proto.Marshal(message)
	if err != nil {
		return err
	}
	return r.client.LPush(ctx, r.key(name), data).Err()
}

// Subscribe blocks waiting for messages from the specified queue and invokes
// the handler for each one. This uses BRPOP with an infinite timeout to wait
// for new messages. The method returns immediately after starting the listener.
func (r *RedisQueue) Subscribe(ctx context.Context, handler queue.MessageHandler) error {
	name, ok := queue.QueueNameFromContext(ctx)
	if !ok {
		name = "default"
	}
	key := r.key(name)

	go func() {
		for {
			res, err := r.client.BRPop(ctx, 0*time.Second, key).Result()
			if err != nil {
				if ctx.Err() != nil {
					return
				}
				// In case of transient errors wait briefly before retrying
				time.Sleep(50 * time.Millisecond)
				continue
			}
			if len(res) != 2 {
				continue
			}
			var msg queuepb.QueueMessage
			if err := proto.Unmarshal([]byte(res[1]), &msg); err != nil {
				continue
			}
			_ = handler(ctx, &msg)
		}
	}()
	return nil
}

// CreateQueue initializes a queue by creating an empty list. Redis creates
// lists on first push so we perform a harmless LPUSH/LPOP sequence to ensure
// the key exists.
func (r *RedisQueue) CreateQueue(ctx context.Context, config *queuepb.QueueConfig) error {
	if config.GetName() == "" {
		return fmt.Errorf("queue name required")
	}
	key := r.key(config.GetName())
	if err := r.client.LPush(ctx, key, "").Err(); err != nil {
		return err
	}
	return r.client.LPop(ctx, key).Err()
}

// DeleteQueue removes the Redis list for the specified queue.
func (r *RedisQueue) DeleteQueue(ctx context.Context, name string) error {
	return r.client.Del(ctx, r.key(name)).Err()
}

// GetQueueInfo retrieves basic statistics for a queue using LLEN.
func (r *RedisQueue) GetQueueInfo(ctx context.Context, name string) (*queuepb.QueueInfo, error) {
	length, err := r.client.LLen(ctx, r.key(name)).Result()
	if err != nil {
		return nil, err
	}
	info := &queuepb.QueueInfo{}
	info.SetName(name)
	info.SetMessageCount(length)
	return info, nil
}

// Close closes the underlying Redis client.
func (r *RedisQueue) Close() error { return r.client.Close() }
