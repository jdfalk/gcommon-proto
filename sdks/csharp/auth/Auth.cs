// file: sdks/csharp/auth/Auth.cs
// version: 1.0.0
// guid: 962e27bf-321b-4837-af5b-0637f23c761b

namespace Sdks.Csharp.Auth;

/// <summary>
/// Authentication helpers.
/// </summary>
public class Auth
{
    private string? _token;

    public string GetToken()
    {
        // TODO: implement token retrieval
        return _token ?? string.Empty;
    }

    public void Refresh()
    {
        // TODO: refresh token
    }

    // TODO: add OAuth2 support
    // TODO: handle JWT validation
    // TODO: support API keys
}
