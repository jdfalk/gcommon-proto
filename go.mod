module github.com/jdfalk/gcommon

go 1.23

require (
	github.com/cockroachdb/pebble v0.0.0-20230928194634-aa077af62593
	github.com/jackc/pgx/v4 v4.18.1
	github.com/lib/pq v1.10.9
	github.com/mattn/go-sqlite3 v1.14.17
	github.com/prometheus/client_golang v1.16.0
	github.com/sirupsen/logrus v1.9.3
	github.com/stretchr/testify v1.8.4
	go.opentelemetry.io/otel v1.19.0
	go.opentelemetry.io/otel/exporters/prometheus v0.42.0
	go.opentelemetry.io/otel/sdk v1.19.0
	go.uber.org/zap v1.24.0
)
