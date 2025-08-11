// file: templates/basic-api-service/main.go
// version: 1.1.0
// guid: 0b45f3d2-3f23-4e96-b8f1-339a9d417f77

// Package main provides a basic API service template integrating gcommon modules.
// The service demonstrates configuration loading, structured logging, metrics
// initialization, and a simple HTTP server. Developers should expand upon this
// template to build production-ready services.
package main

import (
	"context"
	"fmt"
	"net/http"

	gconfig "github.com/jdfalk/gcommon/pkg/config"
	glog "github.com/jdfalk/gcommon/pkg/log"
	gmetrics "github.com/jdfalk/gcommon/pkg/metrics"
	_ "github.com/jdfalk/gcommon/pkg/metrics/prometheus" // register Prometheus provider

	"github.com/jdfalk/gcommon/templates/basic-api-service/internal/config"
	"github.com/jdfalk/gcommon/templates/basic-api-service/internal/server"
)

func main() {
	// Initialize configuration manager and load service configuration.
	cfgMgr := gconfig.NewManager()
	if err := cfgMgr.Load(config.NewFileSource("config/config.yaml")); err != nil {
		panic(fmt.Sprintf("failed to load configuration: %v", err))
	}
	svcCfg := config.MustLoad(cfgMgr)

	// Initialize structured logger using gcommon's logging provider.
	logger, err := glog.NewProvider(glog.Config{Provider: "std", Level: "info"})
	if err != nil {
		panic(fmt.Sprintf("failed to create logger: %v", err))
	}
	defer logger.Close()

	// Initialize metrics provider. Metrics are exposed on a separate port.
	metricsProvider, err := gmetrics.NewProvider(gmetrics.Config{
		Provider:  "prometheus",
		Enabled:   true,
		Namespace: "basic_api_service",
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

	// Create HTTP server with simple health endpoint.
	srv := server.New(svcCfg, logger)

	logger.Info("starting HTTP server", glog.Field{Key: "port", Value: svcCfg.HTTPPort})
	if err := http.ListenAndServe(":"+svcCfg.HTTPPort, srv.Handler()); err != nil {
		logger.Fatal("server failed", glog.Field{Key: "error", Value: err})
	}
}
