// file: sdks/typescript/tests/client.test.ts
// version: 1.1.0
// guid: ba3153bc-572d-4084-81ac-63c194ea95f9

import { Client } from '../client/client';
import { ExampleModel } from '../models/model';
import { ExampleService } from '../services/service';

test('callUnary returns response', async () => {
  const client = new Client();
  await client.connect();
  const svc = new ExampleService(client);
  const model = new ExampleModel('1', 'demo');
  const resp = await svc.call(model);
  expect(resp).toHaveProperty('status', 'ok');
  await client.close();
});

test('callUnary requires connection', async () => {
  const client = new Client();
  await expect(client.callUnary('x', {})).rejects.toThrow();
});
