// file: sdks/csharp/models/Model.cs
// version: 1.0.0
// guid: 9c5098d9-e197-4691-9f6b-d52a99bc8990

namespace Sdks.Csharp.Models;

/// <summary>
/// Example data model.
/// TODO: define properties and validation.
/// </summary>
public class Model
{
    public int Value { get; set; } = 0;

    public bool Validate()
    {
        // TODO: implement validation logic
        return true;
    }

    // TODO: add serialization support
    // TODO: implement equality checks
    // TODO: document usage
}
