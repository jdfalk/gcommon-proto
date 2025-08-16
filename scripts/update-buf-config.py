#!/usr/bin/env python3
# file: scripts/update-buf-config.py  
# version: 1.0.0
# guid: 8b9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e

"""
Update buf.yaml and buf.gen.yaml configurations for the new proto structure.

This script creates the new Buf configurations following the reorganization plan:
1. Updates buf.yaml to point to the new proto/ directory
2. Configures buf.gen.yaml with managed mode for consistent Go package generation  
3. Sets up proper dependencies and plugin configurations
"""

import yaml
import json
from pathlib import Path

def create_new_buf_yaml():
    """Create new buf.yaml configuration."""
    config = {
        'version': 'v2',
        'modules': [
            {
                'path': 'proto',
                'name': 'buf.build/jdfalk/gcommon'
            }
        ],
        'deps': [
            'buf.build/googleapis/googleapis',
            'buf.build/protocolbuffers/wellknowntypes',
            'buf.build/grpc-ecosystem/grpc-gateway'
        ],
        'breaking': {
            'use': ['FILE'],
            'except': [
                'FIELD_SAME_LABEL',
                'EXTENSION_NO_DELETE',
                'FIELD_SAME_DEFAULT'
            ]
        },
        'lint': {
            'use': [
                'STANDARD'
            ],
            'except': [
                'PACKAGE_DIRECTORY_MATCH',
                'PACKAGE_SAME_DIRECTORY', 
                'PACKAGE_VERSION_SUFFIX',
                'IMPORT_NO_PUBLIC',
                'RPC_REQUEST_STANDARD_NAME',
                'RPC_RESPONSE_STANDARD_NAME'
            ],
            'enum_zero_value_suffix': '_UNSPECIFIED',
            'rpc_allow_google_protobuf_empty_requests': True,
            'rpc_allow_google_protobuf_empty_responses': True,
            'service_suffix': 'Service',
            'disallow_comment_ignores': True
        }
    }

    with open('buf.yaml', 'w') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)

    print("✓ Created new buf.yaml")

def create_new_buf_gen_yaml():
    """Create new buf.gen.yaml configuration with managed mode."""
    config = {
        'version': 'v2',
        'managed': {
            'enabled': True,
            'go_package_prefix': {
                'default': 'github.com/jdfalk/gcommon/pkg',
                'override': {
                    'proto/gcommon/v1/common': 'github.com/jdfalk/gcommon/pkg/common',
                    'proto/gcommon/v1/config': 'github.com/jdfalk/gcommon/pkg/config',
                    'proto/gcommon/v1/database': 'github.com/jdfalk/gcommon/pkg/database',
                    'proto/gcommon/v1/media': 'github.com/jdfalk/gcommon/pkg/media',
                    'proto/gcommon/v1/metrics': 'github.com/jdfalk/gcommon/pkg/metrics',
                    'proto/gcommon/v1/organization': 'github.com/jdfalk/gcommon/pkg/organization',
                    'proto/gcommon/v1/queue': 'github.com/jdfalk/gcommon/pkg/queue',
                    'proto/gcommon/v1/web': 'github.com/jdfalk/gcommon/pkg/web'
                }
            },
            'disable': [
                {
                    'file_option': 'go_package_prefix',
                    'module': 'buf.build/googleapis/googleapis'
                }
            ]
        },
        'plugins': [
            {
                'remote': 'buf.build/protocolbuffers/go:v1.36.6',
                'out': 'pkg',
                'opt': [
                    'paths=source_relative',
                    'Mgoogle/protobuf/timestamp.proto=google.golang.org/protobuf/types/known/timestamppb',
                    'Mgoogle/protobuf/duration.proto=google.golang.org/protobuf/types/known/durationpb',
                    'Mgoogle/protobuf/empty.proto=google.golang.org/protobuf/types/known/emptypb',
                    'Mgoogle/protobuf/any.proto=google.golang.org/protobuf/types/known/anypb'
                ]
            },
            {
                'remote': 'buf.build/grpc/go:v1.5.1',
                'out': 'pkg',
                'opt': [
                    'paths=source_relative',
                    'require_unimplemented_servers=false'
                ]
            },
            {
                'remote': 'buf.build/protocolbuffers/python:v5.28.0',
                'out': 'sdks/python'
            },
            {
                'remote': 'buf.build/grpc/python:v1.68.0',
                'out': 'sdks/python'
            }
        ]
    }

    with open('buf.gen.yaml', 'w') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)

    print("✓ Created new buf.gen.yaml")

if __name__ == "__main__":
    # Backup existing files
    for filename in ['buf.yaml', 'buf.gen.yaml']:
        if Path(filename).exists():
            backup_name = f"{filename}.backup"
            Path(filename).rename(backup_name)
            print(f"✓ Backed up {filename} to {backup_name}")

    create_new_buf_yaml()
    create_new_buf_gen_yaml()
    print("✓ Buf configuration files updated for new structure")