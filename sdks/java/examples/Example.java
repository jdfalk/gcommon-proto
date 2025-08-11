// file: sdks/java/examples/Example.java
// version: 1.0.0
// guid: 490c2ad4-bbb1-477f-8d36-41ced52c3041

package sdks.java.examples;

import sdks.java.client.Client;

/**
 * Example usage for Java SDK.
 */
public class Example {
  public static void main(String[] args) {
    Client client = new Client();
    client.connect();
    // TODO: call service methods
    client.close();
  }

  // TODO: add asynchronous example
  // TODO: show authentication usage
}
