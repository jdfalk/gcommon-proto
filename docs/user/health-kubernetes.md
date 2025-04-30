# Integrating Health Checks with Kubernetes

This guide describes how to integrate the `gcommon/pkg/health` module with Kubernetes health probes for effective container health monitoring and orchestration.

## Overview

Kubernetes uses three types of health probes to monitor container health:

1. **Liveness Probe**: Determines if a container is alive. If it fails, Kubernetes restarts the container.
2. **Readiness Probe**: Determines if a container is ready to accept traffic. If it fails, Kubernetes stops sending traffic to the pod.
3. **Startup Probe**: Determines if a container has started successfully. Once it succeeds, the liveness and readiness probes take over.

The `gcommon/pkg/health` module is designed to work seamlessly with these probes through its dedicated HTTP endpoints.

## Configuration

### HTTP Endpoints

The health module exposes the following HTTP endpoints:

- `/health`: Overall health status
- `/health/live`: Liveness check endpoint
- `/health/ready`: Readiness check endpoint
- `/health/details`: Detailed health information for all checks

### Check Types

When registering health checks with the provider, use the appropriate check type:

- `health.TypeLiveness`: For checks related to the application being alive
- `health.TypeReadiness`: For checks related to the application being ready to serve traffic
- `health.TypeComponent`: For internal component checks
- `health.TypeDependency`: For external dependency checks

## Kubernetes Configuration

### Pod Specification

Here's an example of configuring probes in a Kubernetes Pod specification:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-service
spec:
  containers:
  - name: my-service
    image: my-service:latest
    ports:
    - containerPort: 8080
    livenessProbe:
      httpGet:
        path: /health/live
        port: 8080
      initialDelaySeconds: 10
      periodSeconds: 30
      timeoutSeconds: 5
      failureThreshold: 3
    readinessProbe:
      httpGet:
        path: /health/ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 10
      timeoutSeconds: 3
      failureThreshold: 2
    startupProbe:
      httpGet:
        path: /health/live
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
      timeoutSeconds: 3
      failureThreshold: 12  # Allow 1 minute (12 * 5s) to start
```

### Probe Parameters

- `initialDelaySeconds`: Number of seconds after container startup to begin probing
- `periodSeconds`: How often to perform the probe
- `timeoutSeconds`: Number of seconds after which the probe times out
- `successThreshold`: Minimum consecutive successes to be considered successful
- `failureThreshold`: Number of consecutive failures to be considered failed

## Best Practices

### Liveness Probes

Configure liveness checks for:

- Basic application functionality
- System resource monitoring (memory, CPU)
- Core internal services

```go
// Example liveness check registration
provider.Register("system", checks.NewSystemCheck(
    checks.WithMemoryThreshold(90),
),
health.WithType(health.TypeLiveness))
```

### Readiness Probes

Configure readiness checks for:

- External dependencies (databases, APIs)
- Integration points
- Resource availability (connection pools, caches)

```go
// Example readiness check registration
provider.Register("database", checks.NewDBCheck(db,
    checks.WithDBName("main"),
    checks.WithQuery("SELECT 1"),
),
health.WithType(health.TypeReadiness))

provider.Register("external-api", checks.NewHTTPCheck("https://api.example.com/status",
    checks.WithTimeout(3*time.Second),
    checks.WithExpectedStatus(http.StatusOK),
),
health.WithType(health.TypeReadiness))
```

### Remediation and Self-Healing

For non-critical components where automated recovery might be possible:

1. Implement remediable checks:

```go
provider.Register("external-service", checks.NewRemediableHTTPCheck("https://service.example.com/health",
    checks.WithTimeout(5*time.Second),
    checks.WithAlternateURLs("https://service-backup.example.com/health"),
    checks.WithMaxRetries(3),
),
health.WithType(health.TypeReadiness))
```

2. Configure the remediation manager:

```go
config := health.DefaultRemediationConfig()
config.Strategy = health.RemediationStrategyExponential
config.MaxAttempts = 5
config.InitialDelay = 1 * time.Second

remediationMgr := health.NewRemediationManager(provider, config)
remediationMgr.Start(ctx)
```

## Metrics Integration

To observe health check metrics in Kubernetes:

1. Configure Prometheus metrics:

```go
// Set up Prometheus metrics provider
registry := prometheus.NewRegistry()
metricsProvider := health.NewPrometheusMetricsProvider(registry, "myapp")
health.EnableMetricsReporting(healthProvider, metricsProvider)

// Expose metrics endpoint
http.Handle("/metrics", promhttp.HandlerFor(registry, promhttp.HandlerOpts{}))
```

2. Configure Prometheus ServiceMonitor (if using Prometheus Operator):

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: my-service-monitor
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: my-service
  endpoints:
  - port: metrics
    interval: 15s
  namespaceSelector:
    matchNames:
    - default
```

## Health Dashboards

Consider creating Grafana dashboards to visualize:

1. Overall service health status
2. Health check durations
3. Remediation attempts and success rates
4. Correlation between health events and service metrics

## Advanced Configuration

### gRPC Health Probes

To use Kubernetes gRPC probes with our health service:

1. Register both HTTP and gRPC health servers:

```go
// Configure HTTP server with health endpoints
httpMux := http.NewServeMux()
httpMux.Handle("/health/", http.StripPrefix("/health", healthProvider.Handler()))

// Configure gRPC server with health service
grpcServer := grpc.NewServer()
healthServer := health.NewGRPCServer(healthProvider)
healthServer.Register(grpcServer)
```

2. Configure Kubernetes gRPC probes:

```yaml
livenessProbe:
  grpc:
    port: 9090
  initialDelaySeconds: 10
  periodSeconds: 30
```

### Graceful Degradation

Design your health checks to support graceful degradation:

1. Critical dependencies should affect readiness
2. Non-critical dependencies should cause degraded status but not affect readiness
3. Use composite checks to model complex dependencies

```go
// Example of a composite check
serviceCheck := health.NewCompositeCheck("service")
serviceCheck.AddChecks(
    criticalCheck,   // Affects overall status
    nonCriticalCheck // Marked as degraded, doesn't fail the composite
)
provider.Register("service", serviceCheck, health.WithType(health.TypeReadiness))
```

## Troubleshooting

If your pods are being restarted or marked as not ready:

1. Check detailed health status: `kubectl exec -it <pod> -- curl http://localhost:8080/health/details`
2. Check health check logs: `kubectl logs <pod> | grep "health status changed"`
3. Verify probe configuration matches health check configuration
4. Ensure timeouts are configured appropriately for both Kubernetes and health checks

## Conclusion

The `gcommon/pkg/health` module provides a comprehensive solution for implementing Kubernetes health probes that accurately reflect your application's health state. By properly categorizing checks and configuring probes, you can achieve reliable container orchestration with appropriate scaling and recovery behaviors.
