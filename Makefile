# GCommon Makefile
# High-impact development tools for protobuf implementation

.PHONY: help status validate compile test clean quick-wins

help: ## Show this help message
	@echo "🚀 GCommon Development Commands"
	@echo "================================"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

status: ## Get current implementation status
	@echo "📊 Running protobuf coverage analysis..."
	@./validate_protobuf_coverage.py

validate: ## Validate protobuf compilation
	@echo "🔍 Testing protobuf compilation..."
	@./test_protoc.sh

compile: ## Compile all protobuf files
	@echo "🔨 Compiling protobuf files..."
	@./generate.sh

proto-compile: ## Validate protobuf compilation and linting
	@echo "🔍 Validating protobuf files..."
	@./scripts/validate-protos.sh

proto-generate-modules: ## Generate protobuf files per module with detailed reporting
	@echo "🔧 Generating protobuf files per module..."
	@./scripts/buf-generate-per-module.sh

test: ## Run all tests
	@echo "🧪 Running tests..."
	@go test ./... -v

clean: ## Clean all generated files
	@echo "🧹 Cleaning all generated files..."
	@find . -name "*.pb.go" -delete
	@find . -name "*_grpc.pb.go" -delete
	@find . -name "*_mock.go" -delete
	@find . -name "placeholder.go" -delete
	@echo "✅ All generated files cleaned"

clean-rebuild: ## Clean and regenerate all protobuf files and mocks (skip mocks if compilation fails)
	@echo "🔄 Clean rebuild of all protobuf files and mocks..."
	@$(MAKE) clean
	@echo "🔨 Regenerating protobuf files..."
	@buf generate
	@echo "🎭 Attempting to generate mocks..."
	@$(MAKE) generate-mocks || echo "⚠️  Mock generation skipped due to compilation errors (this is expected until all protobuf files are implemented)"
	@echo "✅ Clean rebuild complete"

generate-mocks: ## Generate all mock files using mockery
	@echo "🎭 Generating mocks..."
	@mockery --config .mockery.yml
	@echo "✅ Mocks generated"

force-mocks: ## Force mock generation even with errors
	@echo "🎭 Force generating mocks (ignoring errors)..."
	@mockery --config .mockery.yml || echo "⚠️  Some mocks failed to generate due to compilation errors"
	@echo "✅ Mock generation attempted"

quick-wins: ## Execute high-impact quick wins
	@echo "⚡ Executing quick wins..."
	@$(MAKE) status
	@echo ""
	@echo "🎯 Priority Recommendations:"
	@echo "1. Complete Health module (14 files) - smallest high-priority module"
	@echo "2. Complete Config module (20 files) - second smallest"
	@echo "3. Focus on Cache module (36 files) - good momentum builder"
	@echo ""
	@echo "🔧 Next: make validate && make compile"

# Individual module targets
metrics-status: ## Check metrics module status
	@echo "📊 Metrics Module Status:"
	@find pkg/metrics -name "*.proto" | wc -l | xargs echo "Total files:"
	@find pkg/metrics -name "*.proto" -exec grep -L "message\|service\|enum" {} \; | wc -l | xargs echo "Empty files:"

health-status: ## Check health module status
	@echo "🏥 Health Module Status:"
	@find pkg/health -name "*.proto" | wc -l | xargs echo "Total files:"
	@find pkg/health -name "*.proto" -exec grep -L "message\|service\|enum" {} \; | wc -l | xargs echo "Empty files:"

config-status: ## Check config module status
	@echo "⚙️  Config Module Status:"
	@find pkg/config -name "*.proto" | wc -l | xargs echo "Total files:"
	@find pkg/config -name "*.proto" -exec grep -L "message\|service\|enum" {} \; | wc -l | xargs echo "Empty files:"

# Development workflow helpers
setup-dev: ## Set up development environment
	@echo "🔧 Setting up development environment..."
	@chmod +x *.sh *.py
	@go mod tidy
	@echo "✅ Development environment ready!"

priority-health: ## Start implementing health module (highest ROI)
	@echo "🏥 Health Module Implementation Plan:"
	@echo "Files to implement (14 total):"
	@find pkg/health -name "*.proto" -exec grep -L "message\|service\|enum" {} \; | sort
	@echo ""
	@echo "🎯 Start with: pkg/health/proto/enums/"
	@echo "Then: pkg/health/proto/messages/"
	@echo "Finally: pkg/health/proto/services/"

priority-config: ## Start implementing config module (second highest ROI)
	@echo "⚙️  Config Module Implementation Plan:"
	@echo "Files to implement (20 total):"
	@find pkg/config -name "*.proto" -exec grep -L "message\|service\|enum" {} \; | sort
	@echo ""
	@echo "🎯 Start with: pkg/config/proto/enums/"
	@echo "Then: pkg/config/proto/messages/"
	@echo "Finally: pkg/config/proto/services/"
