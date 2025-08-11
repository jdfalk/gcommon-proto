# file: templates/event-driven-service/Dockerfile
# version: 1.0.0
# guid: ac6d1f39-a9f0-4bde-a059-65930927aa55

FROM golang:1.23 AS builder
WORKDIR /app
COPY . .
RUN go build -o event-driven-service ./...

FROM gcr.io/distroless/base-debian12
WORKDIR /app
COPY --from=builder /app/event-driven-service /app/
EXPOSE 9090
ENTRYPOINT ["/app/event-driven-service"]
