// file: templates/auth-service/main.go
// version: 1.1.0
// guid: de7b176e-9ae6-482b-a70b-bf235d437b49

package main

import (
	"fmt"
	"net/http"

	gconfig "github.com/jdfalk/gcommon/pkg/config"
	glog "github.com/jdfalk/gcommon/pkg/log"

	"github.com/jdfalk/gcommon/templates/auth-service/internal/config"
	"github.com/jdfalk/gcommon/templates/auth-service/internal/server"
)

func main() {
	cfgMgr := gconfig.NewManager()
	if err := cfgMgr.Load(config.NewFileSource("config/config.yaml")); err != nil {
		panic(fmt.Sprintf("config load failed: %v", err))
	}
	cfg := config.MustLoad(cfgMgr)
	logger, _ := glog.NewProvider(glog.Config{Provider: "std"})
	srv := server.New(cfg, logger)
	http.ListenAndServe(":"+cfg.HTTPPort, srv.Handler())
}
