// file: sdks/typescript/auth/auth.ts
// version: 1.1.0
// guid: c037a23e-db76-49ea-ac87-86045feee0ed

export interface OAuth2Config {
  tokenEndpoint: string;
  clientId: string;
  clientSecret: string;
}

export class TokenProvider {
  private token: string | null = null;
  private expires = 0;
  private apiKey: string | null = null;
  private oauth2: OAuth2Config | null = null;

  constructor(init?: { apiKey?: string; oauth2?: OAuth2Config }) {
    this.apiKey = init?.apiKey ?? null;
    this.oauth2 = init?.oauth2 ?? null;
  }

  async getToken(): Promise<string> {
    if (this.apiKey) {
      return this.apiKey;
    }
    const now = Date.now() / 1000;
    if (!this.token || now > this.expires - 30) {
      await this.refresh();
    }
    if (!this.token) {
      throw new Error('token unavailable');
    }
    return this.token;
  }

  async refresh(): Promise<void> {
    if (this.oauth2) {
      const { tokenEndpoint, clientId, clientSecret } = this.oauth2;
      // A real implementation would perform an HTTP POST.  For now we simulate
      // the call to keep the SDK dependency-free.
      void tokenEndpoint; // suppress unused warning
      void clientSecret;
      this.token = `oauth2-${clientId}`;
      this.expires = Date.now() / 1000 + 3600;
      return;
    }
    throw new Error('no refresh mechanism configured');
  }

  setApiKey(key: string): void {
    this.apiKey = key;
    this.token = key;
    this.expires = Number.POSITIVE_INFINITY;
  }

  configureOAuth2(config: OAuth2Config): void {
    this.oauth2 = config;
    this.apiKey = null;
    this.token = null;
    this.expires = 0;
  }
}
