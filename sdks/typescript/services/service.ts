// file: sdks/typescript/services/service.ts
// version: 1.1.0
// guid: 16593558-ea1b-497b-9e7d-9547c7f5f04b

import { Client } from '../client/client';
import { ExampleModel } from '../models/model';

export class ExampleService {
  constructor(private readonly client: Client) {
    this.client.registerUnary('Example/Call', this.callRpc.bind(this));
  }

  private async callRpc(request: unknown): Promise<unknown> {
    const model = ExampleModel.fromJSON(request);
    model.validate();
    return { ...model.toJSON(), status: 'ok' };
  }

  async call(model: ExampleModel): Promise<unknown> {
    model.validate();
    return await this.client.callUnary('Example/Call', model.toJSON());
  }
}
