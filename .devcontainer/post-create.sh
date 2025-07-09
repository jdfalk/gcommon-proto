#!/bin/bash
# file: .devcontainer/post-create.sh
# version: 1.0.0
# guid: f6g7h8i9-j0k1-2345-6789-012345fghijk

set -e

echo "🚀 Setting up GCommon Go/Protobuf development environment..."

# Configure apt and install packages
export DEBIAN_FRONTEND=noninteractive
apt-get update && apt-get -y install --no-install-recommends \
    curl wget unzip git ca-certificates \
    build-essential pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install buf CLI
echo "📦 Installing buf CLI..."
BUF_VERSION="1.47.0"
curl -sSL "https://github.com/bufbuild/buf/releases/download/v${BUF_VERSION}/buf-Linux-x86_64" -o "/usr/local/bin/buf"
chmod +x /usr/local/bin/buf

# Install protoc
echo "📦 Installing protoc..."
PROTOC_VERSION="28.3"
curl -sSL "https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip" -o protoc.zip
unzip protoc.zip -d /usr/local
rm protoc.zip

# Ensure we're in the workspace directory
cd /workspace

# Install Go dependencies
echo "📦 Installing Go dependencies..."
go mod download

# Install Go tools
echo "🔧 Installing Go development tools..."
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
go install golang.org/x/tools/cmd/goimports@latest

# Generate protobuf files
echo "⚙️  Generating protobuf files..."
if [ -f "buf.gen.yaml" ]; then
    buf generate
fi

# Run go generate
echo "⚙️  Running go generate..."
go generate ./...

# Set up git safe directory
echo "🔒 Configuring git safe directory..."
git config --global --add safe.directory /workspace

# Create development directories
echo "📁 Creating development directories..."
mkdir -p /workspace/tmp
mkdir -p /workspace/logs

echo "✅ GCommon development environment setup complete!"
echo ""
echo "🎯 Quick start commands:"
echo "  make all                # Build all packages"
echo "  make test               # Run tests"
echo "  buf lint                # Lint protobuf files"
echo "  buf generate            # Generate protobuf code"
echo "  go build ./...          # Build all Go packages"
echo ""
echo "🔧 Development tools:"
echo "  golangci-lint run       # Lint Go code"
echo "  go fmt ./...            # Format Go code"
echo "  goimports -w .          # Organize imports"
