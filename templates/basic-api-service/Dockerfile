# file: templates/basic-api-service/Dockerfile
# version: 1.0.0
# guid: 105de070-cfba-43a4-8db9-3d771073bf3a

# Dockerfile for the basic API service template. This multi-stage build produces
# a minimal image containing only the compiled binary.

FROM golang:1.23 AS builder
WORKDIR /app
COPY . .
RUN go build -o basic-api-service ./...

FROM gcr.io/distroless/base-debian12
WORKDIR /app
COPY --from=builder /app/basic-api-service /app/
EXPOSE 8080 9090
ENTRYPOINT ["/app/basic-api-service"]

