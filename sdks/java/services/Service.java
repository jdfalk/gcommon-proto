// file: sdks/java/services/Service.java
// version: 1.0.0
// guid: 41f8d6a4-54ec-4752-beb1-c6c2b35f0728

package sdks.java.services;

import sdks.java.client.Client;

/**
 * Example service wrapper.
 */
public class Service {
  private final Client client;

  public Service(Client client) {
    this.client = client;
  }

  public void call() {
    // TODO: implement RPC call
  }

  // TODO: add additional methods
  // TODO: map errors to exceptions
  // TODO: implement retries
  // TODO: document usage
}
