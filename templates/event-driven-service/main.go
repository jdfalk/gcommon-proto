// file: templates/event-driven-service/main.go
// version: 1.1.0
// guid: f2b40dc3-4c58-4dc7-9205-7e2b379def86

// Package main provides an event-driven service template demonstrating queue
// consumption using gcommon's queue module. The service initializes
// configuration, logging, metrics, and starts a background worker that processes
// messages.
package main

import (
	"context"
	"fmt"

	gconfig "github.com/jdfalk/gcommon/pkg/config"
	glog "github.com/jdfalk/gcommon/pkg/log"
	gmetrics "github.com/jdfalk/gcommon/pkg/metrics"
	_ "github.com/jdfalk/gcommon/pkg/metrics/prometheus"
	gqueue "github.com/jdfalk/gcommon/pkg/queue"

	"github.com/jdfalk/gcommon/templates/event-driven-service/internal/config"
	"github.com/jdfalk/gcommon/templates/event-driven-service/internal/worker"
)

func main() {
	cfgMgr := gconfig.NewManager()
	if err := cfgMgr.Load(config.NewFileSource("config/config.yaml")); err != nil {
		panic(fmt.Sprintf("failed to load configuration: %v", err))
	}
	svcCfg := config.MustLoad(cfgMgr)

	logger, err := glog.NewProvider(glog.Config{Provider: "std", Level: "info"})
	if err != nil {
		panic(fmt.Sprintf("failed to create logger: %v", err))
	}
	defer logger.Close()

	metricsProvider, err := gmetrics.NewProvider(gmetrics.Config{
		Provider:  "prometheus",
		Enabled:   true,
		Namespace: "event_driven_service",
	})
	if err != nil {
		logger.Error("failed to create metrics provider", glog.Field{Key: "error", Value: err})
		return
	}
	ctx := context.Background()
	if err := metricsProvider.Start(ctx); err != nil {
		logger.Error("failed to start metrics provider", glog.Field{Key: "error", Value: err})
		return
	}
	defer metricsProvider.Stop(ctx)

	queueProv, err := gqueue.NewProvider(gqueue.Config{Provider: "memory"})
	if err != nil {
		logger.Fatal("queue provider init failed", glog.Field{Key: "error", Value: err})
	}
	defer queueProv.Close()

	w := worker.New(queueProv, logger)
	logger.Info("starting event worker")
	if err := w.Start(ctx); err != nil {
		logger.Fatal("worker failed", glog.Field{Key: "error", Value: err})
	}
}
