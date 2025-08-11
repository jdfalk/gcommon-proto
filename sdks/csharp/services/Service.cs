// file: sdks/csharp/services/Service.cs
// version: 1.0.0
// guid: 2beebf59-6769-48de-8748-1b240967ecb0

using Sdks.Csharp.Client;

namespace Sdks.Csharp.Services;

/// <summary>
/// Example service wrapper.
/// </summary>
public class Service
{
    private readonly Client _client;

    public Service(Client client)
    {
        _client = client;
    }

    public void Call()
    {
        // TODO: implement RPC call
    }

    // TODO: add additional methods
    // TODO: handle errors
    // TODO: include retries
    // TODO: add documentation
}
