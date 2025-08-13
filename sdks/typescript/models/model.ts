// file: sdks/typescript/models/model.ts
// version: 1.1.0
// guid: 6e866da9-dfde-48f0-b6aa-334a7dfccc3c

export class ExampleModel {
  constructor(
    public id: string,
    public name: string,
    public metadata: Record<string, string> = {}
  ) {}

  validate(): void {
    if (!this.id) {
      throw new Error('id is required');
    }
    if (!this.name) {
      throw new Error('name is required');
    }
  }

  toJSON(): Record<string, unknown> {
    return { id: this.id, name: this.name, metadata: { ...this.metadata } };
  }

  static fromJSON(data: unknown): ExampleModel {
    const obj = data as Record<string, unknown>;
    const id = String(obj.id ?? '');
    const name = String(obj.name ?? '');
    const metadata = (obj.metadata as Record<string, string>) || {};
    return new ExampleModel(id, name, metadata);
  }
}
