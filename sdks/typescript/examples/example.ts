// file: sdks/typescript/examples/example.ts
// version: 1.1.0
// guid: 7db6e576-14c7-4a69-a71d-abbdd60fbd4e

import { Client } from '../client/client';
import { ExampleModel } from '../models/model';
import { ExampleService } from '../services/service';

export async function basicExample(): Promise<void> {
  const client = new Client();
  await client.connect();
  try {
    const service = new ExampleService(client);
    const model = new ExampleModel('1', 'demo');
    const resp = await service.call(model);
    console.log(resp);
  } finally {
    await client.close();
  }
}

// TODO: Add authentication example
// TODO: Demonstrate error handling
// TODO: Show streaming usage
