// file: sdks/csharp/tests/ClientTests.cs
// version: 1.0.0
// guid: 063707b3-f325-4976-a300-969c0d0deba5

using Sdks.Csharp.Client;
using Xunit;

namespace Sdks.Csharp.Tests;

public class ClientTests
{
    [Fact]
    public void ClientStub()
    {
        var client = new Client();
        client.Connect();
        // TODO: invoke client methods
        client.Close();
    }

    // TODO: add more tests
    // TODO: cover error cases
    // TODO: include integration tests
}
