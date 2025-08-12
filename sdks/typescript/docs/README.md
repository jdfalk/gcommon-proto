<!-- file: sdks/typescript/docs/README.md -->
<!-- version: 1.1.0 -->
<!-- guid: 5c388dff-311d-46b5-b0a5-836691b01004 -->

# TypeScript Client SDK

The TypeScript SDK provides a promise-based client and basic service wrappers.

## Quick Start

```ts
import { Client } from '../client/client';
import { ExampleModel } from '../models/model';
import { ExampleService } from '../services/service';

const client = new Client();
await client.connect();
const svc = new ExampleService(client);
const model = new ExampleModel('1', 'demo');
await svc.call(model);
await client.close();
```

## Features

- Promise-based API
- Configurable TokenProvider
- ExampleService demonstrating unary RPC calls
- Jest tests for basic behaviours