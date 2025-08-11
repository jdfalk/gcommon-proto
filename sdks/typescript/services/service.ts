// file: sdks/typescript/services/service.ts
// version: 1.0.0
// guid: 16593558-ea1b-497b-9e7d-9547c7f5f04b

import { Client } from '../client/client';

export class ExampleService {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  async call(data: unknown): Promise<unknown> {
    // TODO: implement RPC call via client
    return null;
  }

  // TODO: Add more service methods
  // TODO: Map errors to exceptions
  // TODO: Support retries
  // TODO: Document usage
}
