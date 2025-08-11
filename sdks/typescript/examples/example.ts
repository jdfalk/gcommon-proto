// file: sdks/typescript/examples/example.ts
// version: 1.0.0
// guid: 7db6e576-14c7-4a69-a71d-abbdd60fbd4e

import { Client } from '../client/client';

export async function basicExample(): Promise<void> {
  const client = new Client();
  await client.connect();
  try {
    // TODO: invoke service calls
    console.log('TODO: call service method');
  } finally {
    await client.close();
  }
}

// TODO: Add authentication example
// TODO: Demonstrate error handling
// TODO: Show streaming usage
