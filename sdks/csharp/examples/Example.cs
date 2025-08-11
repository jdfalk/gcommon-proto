// file: sdks/csharp/examples/Example.cs
// version: 1.0.0
// guid: 96508978-96d9-47af-a9b9-7e55fb99f69c

using Sdks.Csharp.Client;

namespace Sdks.Csharp.Examples;

public static class Example
{
    public static void Run()
    {
        var client = new Client();
        client.Connect();
        // TODO: call service methods
        client.Close();
    }

    // TODO: add authentication example
    // TODO: show error handling
}
