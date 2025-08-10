# file: deploy/docker/Dockerfile
# version: 1.1.0
# guid: 33c96dd2-4630-4780-859d-f6ba16ec9719

# ------------------------------------------------------------
# Multi-stage Dockerfile for gcommon-based applications
# Provides build, development, and production stages with
# security hardening and optional debugging tools.
# ------------------------------------------------------------

# ---------- Base Build Stage ----------
FROM golang:1.22-alpine AS builder

# Enable modules and configure work directory
ENV CGO_ENABLED=0 \
    GO111MODULE=on \
    GOPROXY=https://proxy.golang.org,direct

WORKDIR /app

# Cache dependencies
COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg/mod \
    go mod download

# Copy source
COPY . .

# Build main application; override CMD_PATH for specific binaries
ARG CMD_PATH=./cmd/examples
RUN --mount=type=cache,target=/root/.cache/go-build \
    GOOS=linux GOARCH=amd64 go build -trimpath -ldflags "-s -w" -o /gcommon-app ${CMD_PATH}

# ---------- Development Stage ----------
FROM golang:1.22-alpine AS development

WORKDIR /workspace

# Install debugging tools
RUN apk add --no-cache bash curl git && \
    adduser -D devuser
USER devuser

COPY --from=builder /app /workspace

CMD ["go", "test", "./..."]

# ---------- Production Stage ----------
FROM alpine:3.19 AS runtime

LABEL maintainer="gcommon maintainers"

# Install CA certificates and minimal utilities
RUN apk add --no-cache ca-certificates tzdata && \
    adduser -D -u 10001 appuser

WORKDIR /home/appuser

# Copy built binary
COPY --from=builder /gcommon-app /usr/local/bin/app

# Drop privileges
USER appuser

# Expose port and define health check command placeholder
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s \
  CMD wget -qO- http://localhost:8080/health || exit 1

ENTRYPOINT ["/usr/local/bin/app"]
