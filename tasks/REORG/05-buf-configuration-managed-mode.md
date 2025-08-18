<!-- file: tasks/REORG/05-buf-configuration-managed-mode.md -->
<!-- version: 1.0.0 -->
<!-- guid: b6c7d8e9-f0a1-2b3c-4d5e-6f7a8b9c0d1e -->

# Section 05: Buf Configuration and Managed Mode

## 05.1 Buf Workspace Configuration

### 05.1.1 Root buf.yaml Configuration

```yaml
# file: buf.yaml
# version: 1.0.0
# guid: c7d8e9f0-a1b2-3c4d-5e6f-7a8b9c0d1e2f

version: v2
modules:
  - path: proto
    name: buf.build/jdfalk/gcommon

deps:
  - buf.build/googleapis/googleapis
  - buf.build/protocolbuffers/wellknowntypes
  - buf.build/grpc-ecosystem/grpc-gateway

breaking:
  use:
    - FILE
  except:
    - FIELD_SAME_LABEL

lint:
  use:
    - BASIC
    - COMMENTS
    - MINIMAL
  except:
    - PACKAGE_VERSION_SUFFIX
    - SERVICE_SUFFIX
  enum_zero_value_suffix: _UNSPECIFIED
  rpc_allow_same_request_response: false
  rpc_allow_google_protobuf_empty_requests: true
  rpc_allow_google_protobuf_empty_responses: true
  service_suffix: Service
  package_version_suffix: v1

build:
  exclude_imports: true
```

### 05.1.2 Module-specific buf.yaml

```yaml
# file: proto/buf.yaml
# version: 1.0.0
# guid: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a

version: v2
name: buf.build/jdfalk/gcommon
deps:
  - buf.build/googleapis/googleapis
  - buf.build/protocolbuffers/wellknowntypes
  - buf.build/grpc-ecosystem/grpc-gateway

breaking:
  use:
    - FILE
  except:
    - FIELD_SAME_LABEL

lint:
  use:
    - BASIC
    - COMMENTS
    - MINIMAL
  except:
    - PACKAGE_VERSION_SUFFIX
  enum_zero_value_suffix: _UNSPECIFIED
  rpc_allow_same_request_response: false
  rpc_allow_google_protobuf_empty_requests: true
  rpc_allow_google_protobuf_empty_responses: true

build:
  exclude_imports: false
```

### 05.1.3 buf.gen.yaml for Code Generation

```yaml
# file: buf.gen.yaml
# version: 1.0.0
# guid: e9f0a1b2-c3d4-5e6f-7a8b-9c0d1e2f3a4b

version: v2
managed:
  enabled: true
  disable:
    - module: buf.build/googleapis/googleapis
      path: google/api
    - module: buf.build/protocolbuffers/wellknowntypes
      path: google/protobuf
  override:
    - module: buf.build/jdfalk/gcommon
      go_package_prefix:
        default: github.com/jdfalk/gcommon/internal/generated
        except:
          - module_path: gcommon/v1/common
            prefix: github.com/jdfalk/gcommon/internal/generated/common
          - module_path: gcommon/v1/config
            prefix: github.com/jdfalk/gcommon/internal/generated/config
          - module_path: gcommon/v1/database
            prefix: github.com/jdfalk/gcommon/internal/generated/database
          - module_path: gcommon/v1/media
            prefix: github.com/jdfalk/gcommon/internal/generated/media
          - module_path: gcommon/v1/metrics
            prefix: github.com/jdfalk/gcommon/internal/generated/metrics
          - module_path: gcommon/v1/organization
            prefix: github.com/jdfalk/gcommon/internal/generated/organization
          - module_path: gcommon/v1/queue
            prefix: github.com/jdfalk/gcommon/internal/generated/queue
          - module_path: gcommon/v1/web
            prefix: github.com/jdfalk/gcommon/internal/generated/web

plugins:
  - remote: buf.build/protocolbuffers/go
    out: internal/generated
    opt:
      - paths=source_relative
      - module=github.com/jdfalk/gcommon

  - remote: buf.build/grpc/go
    out: internal/generated
    opt:
      - paths=source_relative
      - require_unimplemented_servers=false

  - remote: buf.build/grpc-ecosystem/gateway
    out: internal/generated
    opt:
      - paths=source_relative
      - generate_unbound_methods=true

  - remote: buf.build/grpc-ecosystem/openapiv2
    out: docs/api
    opt:
      - allow_merge=true
      - merge_file_name=gcommon

inputs:
  - module: proto
    include_imports: false
```

## 05.2 Managed Mode Implementation

### 05.2.1 Managed Mode Configuration Script

```python
#!/usr/bin/env python3
# file: scripts/configure-managed-mode.py
# version: 1.0.0
# guid: f0a1b2c3-d4e5-6f7a-8b9c-0d1e2f3a4b5c

import yaml
import json
import os
from pathlib import Path
from typing import Dict, List, Any

class ManagedModeConfigurator:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.proto_dir = self.root_dir / "proto"
        self.config_templates = {}

    def load_configuration_templates(self) -> None:
        """Load configuration templates for different file types."""
        self.config_templates = {
            "buf_yaml": {
                "version": "v2",
                "name": "buf.build/jdfalk/gcommon",
                "deps": [
                    "buf.build/googleapis/googleapis",
                    "buf.build/protocolbuffers/wellknowntypes",
                    "buf.build/grpc-ecosystem/grpc-gateway"
                ],
                "breaking": {
                    "use": ["FILE"],
                    "except": ["FIELD_SAME_LABEL"]
                },
                "lint": {
                    "use": ["BASIC", "COMMENTS", "MINIMAL"],
                    "except": ["PACKAGE_VERSION_SUFFIX"],
                    "enum_zero_value_suffix": "_UNSPECIFIED",
                    "rpc_allow_same_request_response": False,
                    "rpc_allow_google_protobuf_empty_requests": True,
                    "rpc_allow_google_protobuf_empty_responses": True
                },
                "build": {
                    "exclude_imports": False
                }
            },
            "buf_gen_yaml": {
                "version": "v2",
                "managed": {
                    "enabled": True,
                    "disable": [
                        {"module": "buf.build/googleapis/googleapis", "path": "google/api"},
                        {"module": "buf.build/protocolbuffers/wellknowntypes", "path": "google/protobuf"}
                    ],
                    "override": []
                },
                "plugins": [],
                "inputs": [
                    {"module": "proto", "include_imports": False}
                ]
            }
        }

    def generate_go_package_overrides(self) -> List[Dict[str, Any]]:
        """Generate go_package overrides for managed mode."""
        domains = ["common", "config", "database", "media", "metrics", "organization", "queue", "web"]
        base_prefix = "github.com/jdfalk/gcommon/internal/generated"

        overrides = [{
            "module": "buf.build/jdfalk/gcommon",
            "go_package_prefix": {
                "default": base_prefix,
                "except": []
            }
        }]

        # Add domain-specific overrides
        for domain in domains:
            overrides[0]["go_package_prefix"]["except"].append({
                "module_path": f"gcommon/v1/{domain}",
                "prefix": f"{base_prefix}/{domain}"
            })

        return overrides

    def generate_plugin_configuration(self) -> List[Dict[str, Any]]:
        """Generate plugin configuration for code generation."""
        return [
            {
                "remote": "buf.build/protocolbuffers/go",
                "out": "internal/generated",
                "opt": [
                    "paths=source_relative",
                    "module=github.com/jdfalk/gcommon"
                ]
            },
            {
                "remote": "buf.build/grpc/go",
                "out": "internal/generated",
                "opt": [
                    "paths=source_relative",
                    "require_unimplemented_servers=false"
                ]
            },
            {
                "remote": "buf.build/grpc-ecosystem/gateway",
                "out": "internal/generated",
                "opt": [
                    "paths=source_relative",
                    "generate_unbound_methods=true"
                ]
            },
            {
                "remote": "buf.build/grpc-ecosystem/openapiv2",
                "out": "docs/api",
                "opt": [
                    "allow_merge=true",
                    "merge_file_name=gcommon"
                ]
            }
        ]

    def write_buf_yaml(self) -> None:
        """Write the buf.yaml configuration file."""
        config = self.config_templates["buf_yaml"].copy()

        buf_yaml_path = self.proto_dir / "buf.yaml"
        buf_yaml_path.parent.mkdir(parents=True, exist_ok=True)

        with open(buf_yaml_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)

        print(f"Generated {buf_yaml_path}")

    def write_buf_gen_yaml(self) -> None:
        """Write the buf.gen.yaml configuration file."""
        config = self.config_templates["buf_gen_yaml"].copy()

        # Add generated configurations
        config["managed"]["override"] = self.generate_go_package_overrides()
        config["plugins"] = self.generate_plugin_configuration()

        buf_gen_yaml_path = self.root_dir / "buf.gen.yaml"

        with open(buf_gen_yaml_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)

        print(f"Generated {buf_gen_yaml_path}")

    def write_workspace_buf_yaml(self) -> None:
        """Write the workspace-level buf.yaml."""
        workspace_config = {
            "version": "v2",
            "modules": [
                {
                    "path": "proto",
                    "name": "buf.build/jdfalk/gcommon"
                }
            ],
            "deps": [
                "buf.build/googleapis/googleapis",
                "buf.build/protocolbuffers/wellknowntypes",
                "buf.build/grpc-ecosystem/grpc-gateway"
            ],
            "breaking": {
                "use": ["FILE"],
                "except": ["FIELD_SAME_LABEL"]
            },
            "lint": {
                "use": ["BASIC", "COMMENTS", "MINIMAL"],
                "except": ["PACKAGE_VERSION_SUFFIX", "SERVICE_SUFFIX"],
                "enum_zero_value_suffix": "_UNSPECIFIED",
                "rpc_allow_same_request_response": False,
                "rpc_allow_google_protobuf_empty_requests": True,
                "rpc_allow_google_protobuf_empty_responses": True,
                "service_suffix": "Service",
                "package_version_suffix": "v1"
            },
            "build": {
                "exclude_imports": True
            }
        }

        workspace_buf_yaml = self.root_dir / "buf.yaml"

        with open(workspace_buf_yaml, 'w') as f:
            yaml.dump(workspace_config, f, default_flow_style=False, sort_keys=False)

        print(f"Generated {workspace_buf_yaml}")

    def validate_configuration(self) -> bool:
        """Validate the generated configuration."""
        try:
            # Test buf configuration
            import subprocess

            # Check buf.yaml validity
            result = subprocess.run(
                ['buf', 'config', 'ls-modules'],
                cwd=self.root_dir,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print(f"buf config validation failed: {result.stderr}")
                return False

            # Check buf.gen.yaml validity
            result = subprocess.run(
                ['buf', 'generate', '--dry-run'],
                cwd=self.root_dir,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print(f"buf.gen.yaml validation failed: {result.stderr}")
                return False

            print("Configuration validation passed")
            return True

        except Exception as e:
            print(f"Validation error: {e}")
            return False

    def run_configuration(self) -> bool:
        """Run the complete configuration process."""
        print("Configuring managed mode...")

        self.load_configuration_templates()

        # Create configuration files
        self.write_workspace_buf_yaml()
        self.write_buf_yaml()
        self.write_buf_gen_yaml()

        # Validate configuration
        if self.validate_configuration():
            print("Managed mode configuration completed successfully!")
            return True
        else:
            print("Managed mode configuration failed validation!")
            return False

def main():
    configurator = ManagedModeConfigurator('.')
    success = configurator.run_configuration()

    if not success:
        exit(1)

if __name__ == "__main__":
    main()
```

### 05.2.2 Go Package Prefix Management

```go
// file: scripts/manage-go-packages.go
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"text/template"
)

type GoPackageManager struct {
	RootDir     string
	ProtoDir    string
	GeneratedDir string
	ModulePath  string
}

type DomainConfig struct {
	Name       string
	Path       string
	GoPackage  string
	ProtoFiles []string
}

func NewGoPackageManager(rootDir string) *GoPackageManager {
	return &GoPackageManager{
		RootDir:     rootDir,
		ProtoDir:    filepath.Join(rootDir, "proto", "gcommon", "v1"),
		GeneratedDir: filepath.Join(rootDir, "internal", "generated"),
		ModulePath:  "github.com/jdfalk/gcommon",
	}
}

func (gpm *GoPackageManager) DiscoverDomains() ([]DomainConfig, error) {
	domains := []DomainConfig{}

	// Walk through proto directory to find domains
	err := filepath.Walk(gpm.ProtoDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if info.IsDir() && path != gpm.ProtoDir {
			relPath, err := filepath.Rel(gpm.ProtoDir, path)
			if err != nil {
				return err
			}

			// Check if this is a top-level domain
			pathParts := strings.Split(relPath, string(filepath.Separator))
			if len(pathParts) == 1 {
				domain := DomainConfig{
					Name: pathParts[0],
					Path: path,
					GoPackage: fmt.Sprintf("%s/internal/generated/%s", gpm.ModulePath, pathParts[0]),
				}

				// Find proto files in this domain
				protoFiles, err := gpm.findProtoFiles(path)
				if err != nil {
					return err
				}
				domain.ProtoFiles = protoFiles

				domains = append(domains, domain)
			}
		}

		return nil
	})

	return domains, err
}

func (gpm *GoPackageManager) findProtoFiles(dir string) ([]string, error) {
	files := []string{}

	err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if strings.HasSuffix(path, ".proto") {
			files = append(files, path)
		}

		return nil
	})

	return files, err
}

func (gpm *GoPackageManager) GenerateGoModTemplate() (string, error) {
	tmpl := `module {{ .ModulePath }}

go 1.21

require (
	google.golang.org/grpc v1.59.0
	google.golang.org/protobuf v1.31.0
	github.com/grpc-ecosystem/grpc-gateway/v2 v2.18.0
)

require (
	github.com/golang/protobuf v1.5.3 // indirect
	golang.org/x/net v0.17.0 // indirect
	golang.org/x/sys v0.13.0 // indirect
	golang.org/x/text v0.13.0 // indirect
	google.golang.org/genproto v0.0.0-20231016165738-49dd2c1f3d0b // indirect
	google.golang.org/genproto/googleapis/api v0.0.0-20231016165738-49dd2c1f3d0b // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20231016165738-49dd2c1f3d0b // indirect
)
`

	t := template.Must(template.New("gomod").Parse(tmpl))
	var result strings.Builder

	err := t.Execute(&result, map[string]string{
		"ModulePath": gpm.ModulePath,
	})

	return result.String(), err
}

func (gpm *GoPackageManager) UpdateGoOptions() error {
	domains, err := gpm.DiscoverDomains()
	if err != nil {
		return fmt.Errorf("discovering domains: %w", err)
	}

	for _, domain := range domains {
		err := gpm.updateDomainGoOptions(domain)
		if err != nil {
			return fmt.Errorf("updating domain %s: %w", domain.Name, err)
		}
	}

	return nil
}

func (gpm *GoPackageManager) updateDomainGoOptions(domain DomainConfig) error {
	for _, protoFile := range domain.ProtoFiles {
		err := gpm.updateProtoFileGoOption(protoFile, domain.GoPackage)
		if err != nil {
			return fmt.Errorf("updating proto file %s: %w", protoFile, err)
		}
	}

	return nil
}

func (gpm *GoPackageManager) updateProtoFileGoOption(protoFile string, goPackage string) error {
	content, err := os.ReadFile(protoFile)
	if err != nil {
		return fmt.Errorf("reading proto file: %w", err)
	}

	contentStr := string(content)

	// Check if go_package option already exists
	goPackageRegex := regexp.MustCompile(`option\s+go_package\s*=\s*"[^"]*";`)

	if goPackageRegex.MatchString(contentStr) {
		// Update existing go_package option
		contentStr = goPackageRegex.ReplaceAllString(contentStr, fmt.Sprintf(`option go_package = "%s";`, goPackage))
	} else {
		// Add go_package option after package declaration
		packageRegex := regexp.MustCompile(`(package\s+[^;]+;)`)
		if packageRegex.MatchString(contentStr) {
			replacement := fmt.Sprintf("$1\n\noption go_package = \"%s\";", goPackage)
			contentStr = packageRegex.ReplaceAllString(contentStr, replacement)
		}
	}

	err = os.WriteFile(protoFile, []byte(contentStr), 0644)
	if err != nil {
		return fmt.Errorf("writing proto file: %w", err)
	}

	fmt.Printf("Updated go_package in %s\n", protoFile)
	return nil
}

func (gpm *GoPackageManager) GeneratePackageIndex() error {
	domains, err := gpm.DiscoverDomains()
	if err != nil {
		return fmt.Errorf("discovering domains: %w", err)
	}

	indexContent := `// file: internal/generated/index.go
// version: 1.0.0
// guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

// Package generated contains all generated protobuf code for gcommon.
package generated

// Domain packages:
`

	for _, domain := range domains {
		indexContent += fmt.Sprintf("// - %s: %s\n", domain.Name, domain.GoPackage)
	}

	indexPath := filepath.Join(gpm.GeneratedDir, "index.go")

	// Create directory if it doesn't exist
	err = os.MkdirAll(filepath.Dir(indexPath), 0755)
	if err != nil {
		return fmt.Errorf("creating directory: %w", err)
	}

	err = os.WriteFile(indexPath, []byte(indexContent), 0644)
	if err != nil {
		return fmt.Errorf("writing index file: %w", err)
	}

	fmt.Printf("Generated package index: %s\n", indexPath)
	return nil
}

func (gpm *GoPackageManager) GenerateReport() error {
	domains, err := gpm.DiscoverDomains()
	if err != nil {
		return fmt.Errorf("discovering domains: %w", err)
	}

	report := fmt.Sprintf(`# Go Package Management Report

Generated on: %s
Module Path: %s
Proto Directory: %s
Generated Directory: %s

## Domain Configuration

`, "{{.Timestamp}}", gpm.ModulePath, gpm.ProtoDir, gpm.GeneratedDir)

	for _, domain := range domains {
		report += fmt.Sprintf(`### %s Domain
- Path: %s
- Go Package: %s
- Proto Files: %d

`, domain.Name, domain.Path, domain.GoPackage, len(domain.ProtoFiles))
	}

	report += `## Generated Files Structure

`

	// Add file structure
	err = filepath.Walk(gpm.GeneratedDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if !info.IsDir() {
			relPath, _ := filepath.Rel(gpm.GeneratedDir, path)
			report += fmt.Sprintf("- %s\n", relPath)
		}

		return nil
	})

	if err != nil {
		return fmt.Errorf("walking generated directory: %w", err)
	}

	reportPath := filepath.Join(gpm.RootDir, "go-package-report.md")
	err = os.WriteFile(reportPath, []byte(report), 0644)
	if err != nil {
		return fmt.Errorf("writing report: %w", err)
	}

	fmt.Printf("Generated package report: %s\n", reportPath)
	return nil
}

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s <command>\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "Commands: update-options, generate-index, generate-report\n")
		os.Exit(1)
	}

	command := os.Args[1]
	manager := NewGoPackageManager(".")

	switch command {
	case "update-options":
		err := manager.UpdateGoOptions()
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error updating go options: %v\n", err)
			os.Exit(1)
		}
		fmt.Println("Go options updated successfully")

	case "generate-index":
		err := manager.GeneratePackageIndex()
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error generating package index: %v\n", err)
			os.Exit(1)
		}

	case "generate-report":
		err := manager.GenerateReport()
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error generating report: %v\n", err)
			os.Exit(1)
		}

	default:
		fmt.Fprintf(os.Stderr, "Unknown command: %s\n", command)
		os.Exit(1)
	}
}
```

## 05.3 Dependency Management

### 05.3.1 External Dependency Configuration

```yaml
# file: dependencies.yaml
# version: 1.0.0
# guid: c4d5e6f7-a8b9-0c1d-2e3f-4a5b6c7d8e9f

dependencies:
  external:
    googleapis:
      source: buf.build/googleapis/googleapis
      version: latest
      paths:
        - google/api
        - google/rpc
        - google/type
        - google/longrunning
      purpose: 'Google API definitions and common types'

    wellknowntypes:
      source: buf.build/protocolbuffers/wellknowntypes
      version: latest
      paths:
        - google/protobuf
      purpose: 'Standard protobuf well-known types'

    grpc_gateway:
      source: buf.build/grpc-ecosystem/grpc-gateway
      version: latest
      paths:
        - protoc-gen-openapiv2/options
        - protoc-gen-grpc-gateway/options
      purpose: 'gRPC-Gateway annotations and options'

  internal:
    gcommon:
      module: gcommon.v1
      domains:
        - common
        - config
        - database
        - media
        - metrics
        - organization
        - queue
        - web
      base_path: proto/gcommon/v1

managed_overrides:
  go_package_prefix:
    default: github.com/jdfalk/gcommon/internal/generated
    domains:
      common: github.com/jdfalk/gcommon/internal/generated/common
      config: github.com/jdfalk/gcommon/internal/generated/config
      database: github.com/jdfalk/gcommon/internal/generated/database
      media: github.com/jdfalk/gcommon/internal/generated/media
      metrics: github.com/jdfalk/gcommon/internal/generated/metrics
      organization: github.com/jdfalk/gcommon/internal/generated/organization
      queue: github.com/jdfalk/gcommon/internal/generated/queue
      web: github.com/jdfalk/gcommon/internal/generated/web
```

### 05.3.2 Dependency Version Management Script

```python
#!/usr/bin/env python3
# file: scripts/manage-dependencies.py
# version: 1.0.0
# guid: d5e6f7a8-b9c0-1d2e-3f4a-5b6c7d8e9f0a

import yaml
import json
import requests
import subprocess
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Dependency:
    name: str
    source: str
    version: str
    paths: List[str]
    purpose: str

@dataclass
class VersionInfo:
    current: str
    latest: str
    update_available: bool
    changelog_url: str = ""

class DependencyManager:
    def __init__(self, config_file: str = "dependencies.yaml"):
        self.config_file = Path(config_file)
        self.dependencies = {}
        self.load_configuration()

    def load_configuration(self) -> None:
        """Load dependency configuration from YAML file."""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                config = yaml.safe_load(f)

            for name, info in config.get('dependencies', {}).get('external', {}).items():
                self.dependencies[name] = Dependency(
                    name=name,
                    source=info['source'],
                    version=info['version'],
                    paths=info['paths'],
                    purpose=info['purpose']
                )

    def check_buf_registry_version(self, module_name: str) -> str:
        """Check latest version of a module in buf registry."""
        try:
            # Use buf CLI to check module info
            result = subprocess.run(
                ['buf', 'registry', 'module', 'info', module_name],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                # Parse output to extract version
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if 'Latest Version:' in line:
                        return line.split(':')[1].strip()

            return "unknown"

        except Exception as e:
            print(f"Error checking version for {module_name}: {e}")
            return "unknown"

    def check_version_updates(self) -> Dict[str, VersionInfo]:
        """Check for version updates for all dependencies."""
        version_info = {}

        for name, dep in self.dependencies.items():
            current_version = dep.version
            latest_version = self.check_buf_registry_version(dep.source)

            version_info[name] = VersionInfo(
                current=current_version,
                latest=latest_version,
                update_available=(latest_version != "unknown" and
                                latest_version != current_version and
                                current_version != "latest")
            )

        return version_info

    def update_dependency_versions(self, version_info: Dict[str, VersionInfo]) -> None:
        """Update dependency versions in configuration."""
        config_updated = False

        with open(self.config_file, 'r') as f:
            config = yaml.safe_load(f)

        for name, info in version_info.items():
            if info.update_available:
                # Update version in configuration
                config['dependencies']['external'][name]['version'] = info.latest
                self.dependencies[name].version = info.latest
                config_updated = True
                print(f"Updated {name}: {info.current} -> {info.latest}")

        if config_updated:
            with open(self.config_file, 'w') as f:
                yaml.dump(config, f, default_flow_style=False, sort_keys=False)

        return config_updated

    def update_buf_configurations(self) -> None:
        """Update buf.yaml files with latest dependency versions."""
        # Update workspace buf.yaml
        workspace_buf = Path("buf.yaml")
        if workspace_buf.exists():
            with open(workspace_buf, 'r') as f:
                config = yaml.safe_load(f)

            # Update deps with explicit versions if needed
            deps = []
            for name, dep in self.dependencies.items():
                if dep.version != "latest":
                    deps.append(f"{dep.source}:{dep.version}")
                else:
                    deps.append(dep.source)

            config['deps'] = deps

            with open(workspace_buf, 'w') as f:
                yaml.dump(config, f, default_flow_style=False, sort_keys=False)

        # Update module buf.yaml
        module_buf = Path("proto/buf.yaml")
        if module_buf.exists():
            with open(module_buf, 'r') as f:
                config = yaml.safe_load(f)

            # Update deps
            deps = []
            for name, dep in self.dependencies.items():
                if dep.version != "latest":
                    deps.append(f"{dep.source}:{dep.version}")
                else:
                    deps.append(dep.source)

            config['deps'] = deps

            with open(module_buf, 'w') as f:
                yaml.dump(config, f, default_flow_style=False, sort_keys=False)

    def validate_dependencies(self) -> bool:
        """Validate that all dependencies are accessible."""
        valid = True

        for name, dep in self.dependencies.items():
            try:
                # Use buf to validate dependency
                result = subprocess.run(
                    ['buf', 'registry', 'module', 'info', dep.source],
                    capture_output=True,
                    text=True
                )

                if result.returncode == 0:
                    print(f"✓ {name}: {dep.source} - accessible")
                else:
                    print(f"✗ {name}: {dep.source} - not accessible")
                    valid = False

            except Exception as e:
                print(f"✗ {name}: {dep.source} - error: {e}")
                valid = False

        return valid

    def generate_dependency_report(self, version_info: Dict[str, VersionInfo]) -> str:
        """Generate dependency report."""
        report = f"""# Dependency Management Report

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## External Dependencies

| Name | Source | Current Version | Latest Version | Update Available |
| ---- | ------ | --------------- | -------------- | ---------------- |
"""

        for name, info in version_info.items():
            dep = self.dependencies[name]
            update_status = "✓" if info.update_available else "✗"
            report += f"| {name} | {dep.source} | {info.current} | {info.latest} | {update_status} |\n"

        report += "\n## Dependency Purposes\n\n"

        for name, dep in self.dependencies.items():
            report += f"### {name}\n"
            report += f"- **Source**: {dep.source}\n"
            report += f"- **Purpose**: {dep.purpose}\n"
            report += f"- **Paths**: {', '.join(dep.paths)}\n\n"

        return report

    def run_dependency_update(self) -> bool:
        """Run complete dependency update process."""
        print("Checking dependency versions...")
        version_info = self.check_version_updates()

        # Show update summary
        updates_available = sum(1 for info in version_info.values() if info.update_available)
        print(f"Found {updates_available} dependencies with updates available")

        if updates_available > 0:
            print("Updating dependency versions...")
            config_updated = self.update_dependency_versions(version_info)

            if config_updated:
                print("Updating buf configurations...")
                self.update_buf_configurations()

        print("Validating dependencies...")
        if not self.validate_dependencies():
            print("Dependency validation failed!")
            return False

        # Generate report
        report = self.generate_dependency_report(version_info)
        with open("dependency-report.md", 'w') as f:
            f.write(report)

        print("Dependency update completed successfully!")
        print("Report saved to: dependency-report.md")
        return True

def main():
    manager = DependencyManager()
    success = manager.run_dependency_update()

    if not success:
        exit(1)

if __name__ == "__main__":
    main()
```

## 05.4 Code Generation Optimization

### 05.4.1 Build Performance Configuration

```yaml
# file: buf.performance.yaml
# version: 1.0.0
# guid: e6f7a8b9-c0d1-2e3f-4a5b-6c7d8e9f0a1b

version: v2
name: buf.build/jdfalk/gcommon

build:
  exclude_imports: false
  exclude_source_info: false

# Performance optimizations
performance:
  parallel_generation: true
  max_parallel_jobs: 8
  cache_enabled: true
  cache_dir: .buf_cache

# Code generation optimizations
generation:
  incremental: true
  dependency_tracking: true
  output_caching: true

# Linting optimizations
lint:
  parallel: true
  cache_results: true
  incremental_mode: true
```

### 05.4.2 Parallel Generation Script

```bash
#!/bin/bash
# file: scripts/parallel-generation.sh
# version: 1.0.0
# guid: f7a8b9c0-d1e2-3f4a-5b6c-7d8e9f0a1b2c

set -euo pipefail

# Configuration
PROTO_DIR="gcommon/v1"
OUTPUT_DIR="internal/generated"
CACHE_DIR=".buf_cache"
MAX_JOBS="${BUF_MAX_JOBS:-8}"
TEMP_DIR="/tmp/buf-parallel-gen"

# Create necessary directories
mkdir -p "$CACHE_DIR" "$TEMP_DIR" "$OUTPUT_DIR"

# Function to generate code for a single domain
generate_domain() {
    local domain="$1"
    local domain_dir="$PROTO_DIR/$domain"
    local output_subdir="$OUTPUT_DIR/$domain"

    echo "Generating code for domain: $domain"

    # Create domain-specific output directory
    mkdir -p "$output_subdir"

    # Generate code for this domain only
    if buf generate --path "$domain_dir" --template buf.gen.yaml; then
        echo "✓ Generated code for $domain"
        return 0
    else
        echo "✗ Failed to generate code for $domain"
        return 1
    fi
}

# Function to run parallel generation
run_parallel_generation() {
    local domains=()

    # Discover domains
    for domain_dir in "$PROTO_DIR"/*; do
        if [ -d "$domain_dir" ]; then
            domain=$(basename "$domain_dir")
            domains+=("$domain")
        fi
    done

    echo "Found ${#domains[@]} domains: ${domains[*]}"

    # Generate code in parallel
    export -f generate_domain
    export PROTO_DIR OUTPUT_DIR

    printf '%s\n' "${domains[@]}" | xargs -n 1 -P "$MAX_JOBS" -I {} bash -c 'generate_domain "$@"' _ {}
}

# Function to merge generated outputs
merge_outputs() {
    echo "Merging generated outputs..."

    # Create unified package structure
    for domain in "$OUTPUT_DIR"/*; do
        if [ -d "$domain" ]; then
            domain_name=$(basename "$domain")
            echo "Processing domain: $domain_name"

            # Move generated files to proper locations
            find "$domain" -name "*.pb.go" -o -name "*_grpc.pb.go" -o -name "*.pb.gw.go" | while read -r file; do
                # Preserve relative path structure
                rel_path=$(realpath --relative-to="$domain" "$file")
                target_dir="$OUTPUT_DIR/$domain_name/$(dirname "$rel_path")"

                mkdir -p "$target_dir"
                mv "$file" "$target_dir/"
            done
        fi
    done
}

# Function to validate generation results
validate_generation() {
    echo "Validating generation results..."

    # Check that all expected files were generated
    local total_pb_files=0
    local total_grpc_files=0
    local total_gw_files=0

    total_pb_files=$(find "$OUTPUT_DIR" -name "*.pb.go" | wc -l)
    total_grpc_files=$(find "$OUTPUT_DIR" -name "*_grpc.pb.go" | wc -l)
    total_gw_files=$(find "$OUTPUT_DIR" -name "*.pb.gw.go" | wc -l)

    echo "Generated files:"
    echo "  .pb.go files: $total_pb_files"
    echo "  _grpc.pb.go files: $total_grpc_files"
    echo "  .pb.gw.go files: $total_gw_files"

    # Test compilation
    if go build ./internal/generated/...; then
        echo "✓ Generated code compiles successfully"
        return 0
    else
        echo "✗ Generated code compilation failed"
        return 1
    fi
}

# Function to generate performance report
generate_performance_report() {
    local start_time="$1"
    local end_time="$2"
    local duration=$((end_time - start_time))

    cat > "generation-performance-report.md" << EOF
# Code Generation Performance Report

Generated on: $(date)
Duration: ${duration} seconds
Max Parallel Jobs: $MAX_JOBS

## Statistics
EOF

    echo "- Total .pb.go files: $(find "$OUTPUT_DIR" -name "*.pb.go" | wc -l)" >> "generation-performance-report.md"
    echo "- Total _grpc.pb.go files: $(find "$OUTPUT_DIR" -name "*_grpc.pb.go" | wc -l)" >> "generation-performance-report.md"
    echo "- Total .pb.gw.go files: $(find "$OUTPUT_DIR" -name "*.pb.gw.go" | wc -l)" >> "generation-performance-report.md"
    echo "- Output directory size: $(du -sh "$OUTPUT_DIR" | cut -f1)" >> "generation-performance-report.md"

    cat >> "generation-performance-report.md" << EOF

## Performance Metrics
- Generation time: ${duration} seconds
- Parallel jobs used: $MAX_JOBS
- Cache directory: $CACHE_DIR

## Domain Breakdown
EOF

    for domain_dir in "$OUTPUT_DIR"/*; do
        if [ -d "$domain_dir" ]; then
            domain=$(basename "$domain_dir")
            file_count=$(find "$domain_dir" -name "*.pb.go" | wc -l)
            echo "- $domain: $file_count files" >> "generation-performance-report.md"
        fi
    done
}

# Main execution
main() {
    local start_time=$(date +%s)

    echo "Starting parallel code generation..."
    echo "Max parallel jobs: $MAX_JOBS"
    echo "Proto directory: $PROTO_DIR"
    echo "Output directory: $OUTPUT_DIR"

    # Clean previous output
    if [ -d "$OUTPUT_DIR" ]; then
        echo "Cleaning previous output..."
        rm -rf "$OUTPUT_DIR"
    fi

    # Run parallel generation
    if run_parallel_generation; then
        echo "Parallel generation completed"
    else
        echo "Parallel generation failed"
        exit 1
    fi

    # Merge outputs
    merge_outputs

    # Validate results
    if validate_generation; then
        echo "Validation passed"
    else
        echo "Validation failed"
        exit 1
    fi

    local end_time=$(date +%s)

    # Generate performance report
    generate_performance_report "$start_time" "$end_time"

    echo "Parallel code generation completed successfully!"
    echo "Performance report: generation-performance-report.md"
}

# Cleanup function
cleanup() {
    rm -rf "$TEMP_DIR"
}

# Set up cleanup trap
trap cleanup EXIT

# Run main function
main "$@"
```

This section provides comprehensive buf configuration and managed mode implementation for the protobuf reorganization, including dependency management, performance optimization, and parallel code generation strategies.
