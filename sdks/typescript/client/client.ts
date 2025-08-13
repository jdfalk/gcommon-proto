// file: sdks/typescript/client/client.ts
// version: 1.1.0
// guid: 75c87cb1-3d78-4dd9-bb0d-e90ec4e454e0

import { TokenProvider } from '../auth/auth';

export type UnaryHandler = (
  req: unknown,
  metadata: Record<string, string>
) => Promise<unknown>;

export class Client {
  private readonly handlers: Record<string, UnaryHandler> = {};
  private connected = false;

  constructor(
    private readonly address = 'http://localhost:8080',
    private readonly tokenProvider: TokenProvider | null = null
  ) {}

  async connect(): Promise<void> {
    this.connected = true;
  }

  async close(): Promise<void> {
    this.connected = false;
  }

  registerUnary(name: string, handler: UnaryHandler): void {
    this.handlers[name] = handler;
  }

  async callUnary(
    name: string,
    data: unknown,
    timeout = 30_000
  ): Promise<unknown> {
    if (!this.connected) {
      throw new Error('client not connected');
    }
    const handler = this.handlers[name];
    if (!handler) {
      throw new Error(`unregistered handler: ${name}`);
    }
    const metadata: Record<string, string> = {};
    if (this.tokenProvider) {
      metadata.authorization = `Bearer ${await this.tokenProvider.getToken()}`;
    }
    return await Promise.race([
      handler(data, metadata),
      new Promise((_, reject) =>
        setTimeout(() => reject(new Error('timeout')), timeout)
      ),
    ]);
  }
}
