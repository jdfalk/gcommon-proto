# Using the Health Module with Kubernetes

This guide explains how to integrate the GCommon health module with Kubernetes health probes and enable metrics collection for health checks.

## Overview

Kubernetes uses [probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) to determine the health of containers in a pod:

- **Liveness Probes**: Determine if an application is running. If a liveness probe fails, Kubernetes will restart the container.
- **Readiness Probes**: Determine if an application is ready to receive traffic. If a readiness probe fails, Kubernetes will remove the pod from service endpoints.
- **Startup Probes**: Determine if an application has started successfully. Startup probes are useful for applications with slow startup times.

The health module in GCommon supports all these probe types through a dedicated Kubernetes integration.

## Setting Up Kubernetes Probes

### Step 1: Create a Health Provider

First, create a health provider with appropriate configuration:

```go
healthConfig := health.Config{
    Enabled:                true,
    CheckInterval:          10 * time.Second,
    DefaultTimeout:         1 * time.Second,
    EnableLivenessEndpoint: true,
    EnableReadinessEndpoint: true,
    LivenessPath:          "/health/live",
    ReadinessPath:         "/health/ready",
    LogStatusChanges:      true,
}

healthProvider, err := health.NewProvider(healthConfig)
if err != nil {
    log.Fatalf("Failed to create health provider: %v", err)
}
```

### Step 2: Register Health Checks

Register health checks for different probe types:

```go
// Liveness checks (verify application is running)
healthProvider.Register("cpu", checks.NewCPUCheck(70.0),
    health.WithType(health.TypeLiveness),
    health.WithInterval(30*time.Second),
)

healthProvider.Register("memory", checks.NewMemoryCheck(80.0),
    health.WithType(health.TypeLiveness),
    health.WithInterval(30*time.Second),
)

// Readiness checks (verify application can serve requests)
healthProvider.Register("database", checks.NewDatabaseCheck(dbPool),
    health.WithType(health.TypeReadiness),
    health.WithTimeout(2*time.Second),
    health.WithInterval(15*time.Second),
)

healthProvider.Register("api-dependency", checks.NewHTTPCheck("https://api.example.com/health"),
    health.WithType(health.TypeReadiness),
    health.WithTimeout(2*time.Second),
    health.WithInterval(15*time.Second),
)
```

### Step 3: Create a Kubernetes Probe Handler

Create a Kubernetes probe handler with appropriate configuration:

```go
probeConfig := health.DefaultKubernetesProbeConfig()
// Optional: customize probe paths and settings
probeConfig.LivenessPath = "/healthz"
probeConfig.ReadinessPath = "/readyz"
probeConfig.StartupPath = "/startupz"
probeConfig.ProbeTimeout = 1 * time.Second

kubeProbeHandler := health.NewKubernetesProbeHandler(healthProvider, probeConfig)
```

### Step 4: Register the Probe Handler with HTTP Server

Register the probe handler with your HTTP server:

```go
mux := http.NewServeMux()

// Register Kubernetes probe handlers
kubeProbeHandler.RegisterWithMux(mux)

// Start the HTTP server
server := &http.Server{
    Addr:    ":8080",
    Handler: mux,
}

go server.ListenAndServe()
```

### Step 5: Configure Kubernetes Pod Specification

Configure your Kubernetes pod to use the health endpoints:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
    - name: app
      image: my-app:latest
      ports:
        - containerPort: 8080
      livenessProbe:
        httpGet:
          path: /healthz
          port: 8080
        initialDelaySeconds: 10
        periodSeconds: 30
        timeoutSeconds: 1
        failureThreshold: 3
      readinessProbe:
        httpGet:
          path: /readyz
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 10
        timeoutSeconds: 1
        failureThreshold: 2
      startupProbe:
        httpGet:
          path: /startupz
          port: 8080
        periodSeconds: 5
        failureThreshold: 12 # Allow 1 minute (12 * 5s) for startup
```

## Collecting Health Check Metrics

The health module can collect metrics about health check execution and status. These metrics can be used to monitor the health of your application over time.

### Step 1: Create a Metrics Provider

First, create a metrics provider:

```go
metricsConfig := metrics.Config{
    Enabled:              true,
    Provider:             "prometheus",
    Namespace:            "myapp",
    Subsystem:            "health",
    EnableRuntimeMetrics: true,
}

metricsProvider, err := metrics.NewProvider(metricsConfig)
if err != nil {
    log.Fatalf("Failed to create metrics provider: %v", err)
}
```

### Step 2: Create a Metrics Collector

Create a metrics collector for health checks:

```go
metricsConfig := health.DefaultMetricsConfig()
// Optional: customize metrics settings
metricsConfig.Prefix = "myapp_health"
metricsConfig.CollectInterval = 15 * time.Second

metricsCollector := health.NewMetricsCollector(healthProvider, metricsProvider, metricsConfig)
```

### Step 3: Start the Metrics Collector

Start the metrics collector:

```go
ctx := context.Background()
if err := metricsCollector.Start(ctx); err != nil {
    log.Fatalf("Failed to start metrics collector: %v", err)
}
```

### Step 4: Expose Metrics Endpoint

Expose the metrics endpoint for Prometheus to scrape:

```go
mux.Handle("/metrics", metricsProvider.Handler())
```

### Step 5: Configure Prometheus Scraping

Configure Prometheus to scrape the metrics endpoint by adding a scrape configuration:

```yaml
scrape_configs:
  - job_name: 'myapp'
    scrape_interval: 15s
    static_configs:
      - targets: ['myapp:8080']
```

## Available Metrics

The health module collects the following metrics:

- `health.status`: Gauge showing the current status of each health check (0=down, 1=degraded, 2=up, 3=unknown)
- `health.executions_total`: Counter of total health check executions
- `health.success_total`: Counter of successful health check executions
- `health.failure_total`: Counter of failed health check executions
- `health.duration_seconds`: Histogram of health check execution duration in seconds

These metrics include labels such as:

- `check`: The name of the health check
- `type`: The type of health check (liveness, readiness, component, dependency)
- `status`: The status of the health check (UP, DOWN, DEGRADED, UNKNOWN)

## Auto-Remediation for Failed Health Checks

The health module supports automatic remediation for failed health checks. This can be useful for services that can self-heal when certain issues are detected.

### Step 1: Create a Remediable Check

Create a health check that implements remediation:

```go
// Custom check with remediation
healthProvider.Register("database-connection",
    checks.NewRemediableHTTPCheck(
        "http://localhost:8080/db/ping",
        func(ctx context.Context, result health.Result) error {
            log.Println("Attempting to reconnect to database...")
            // In a real implementation, this would reconnect to the database
            return dbPool.Reset()
        },
    ),
    health.WithType(health.TypeReadiness),
    health.WithTimeout(1*time.Second),
    health.WithInterval(15*time.Second),
)
```

### Step 2: Create a Remediation Manager

Create a remediation manager with appropriate configuration:

```go
remediationConfig := health.DefaultRemediationConfig()
remediationConfig.Strategy = health.RemediationStrategyExponential
remediationConfig.MaxAttempts = 3
remediationConfig.InitialDelay = 1 * time.Second
remediationConfig.BackoffFactor = 2.0

// Optional: Add callbacks for remediation events
remediationConfig.OnRemediationStart = func(name string, attempt int) {
    log.Printf("Starting remediation for %s (attempt %d)", name, attempt)
}
remediationConfig.OnRemediationSuccess = func(name string, attempt int) {
    log.Printf("Remediation successful for %s (attempt %d)", name, attempt)
}

remediationManager := health.NewRemediationManager(healthProvider, remediationConfig)
```

### Step 3: Start the Remediation Manager

Start the remediation manager:

```go
if err := remediationManager.Start(ctx); err != nil {
    log.Fatalf("Failed to start remediation manager: %v", err)
}
```

## Complete Example

A complete example demonstrating Kubernetes integration, metrics collection, and auto-remediation is available in the `examples/health/kubernetes_integration.go` file.

## Best Practices

1. **Separate Liveness and Readiness Checks**: Use liveness checks for detecting issues that require container restarts, and readiness checks for detecting issues that require temporary removal from load balancing.

2. **Choose Appropriate Timeouts**: Set timeouts that are short enough to detect failures quickly but long enough to avoid false positives.

3. **Monitor Metrics**: Use the collected metrics to identify patterns in health check failures and set up alerts for recurring issues.

4. **Use Auto-Remediation Carefully**: Auto-remediation is useful for known, recoverable issues, but shouldn't mask deeper problems. Always log remediation attempts for later analysis.

5. **Graceful Shutdown**: Implement graceful shutdown to ensure health checks are properly stopped when the application is shutting down.

6. **Test Failure Scenarios**: Regularly test how your application behaves when health checks fail to ensure the desired Kubernetes behaviors occur.
