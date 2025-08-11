# file: templates/auth-service/Dockerfile
# version: 1.0.0
# guid: c300ca1e-10a1-4648-bd33-82075a90a1a4

FROM golang:1.23 AS builder
WORKDIR /app
COPY . .
RUN go build -o auth-service ./...

FROM gcr.io/distroless/base-debian12
WORKDIR /app
COPY --from=builder /app/auth-service /app/
EXPOSE 8080
ENTRYPOINT ["/app/auth-service"]

