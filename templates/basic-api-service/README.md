<!-- file: templates/basic-api-service/README.md -->
<!-- version: 1.0.0 -->
<!-- guid: 1fd546ec-7000-4b7b-a3aa-51e097d15ce3 -->

# Basic API Service Template

This template provides a starting point for building a simple HTTP API using
[gcommon](https://github.com/jdfalk/gcommon) modules. It demonstrates
configuration management, structured logging, metrics integration, and basic
Kubernetes deployment manifests.

## Features

- Configuration loading via gcommon `config` module
- Structured logging with gcommon `log` module
- Metrics collection using gcommon `metrics` module
- Dockerfile and Kubernetes manifests
- GitHub Actions workflow for CI

## Usage

```bash
# Generate a new service from this template
./scripts/generate-microservice.sh basic-api-service ../my-service
```

After generation, customize the service as needed.

# Basic API Service Template\n\nSkeleton service providing a simple API with gcommon integration.
