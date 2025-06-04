module github.com/jdfalk/gcommon/examples/database

go 1.21

require (
	github.com/jdfalk/gcommon v0.0.0
	github.com/jackc/pgx/v4 v4.18.2
	github.com/mattn/go-sqlite3 v1.14.22
	github.com/cockroachdb/pebble v1.1.0
)

replace github.com/jdfalk/gcommon => ../..
