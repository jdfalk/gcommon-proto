<!-- file: sdks/python/docs/README.md -->
<!-- version: 1.1.0 -->
<!-- guid: 9e71fe6e-a036-472d-ad1d-d830d232bd83 -->

# Python Client SDK

This SDK offers an asynchronous client with token-based authentication and service wrappers.

## Quick Start

```python
from sdks.python.client.client import Client
from sdks.python.services.service import ExampleService
from sdks.python.models.model import ExampleModel

async with Client().lifespan() as client:
    service = ExampleService(client)
    model = ExampleModel(identifier="1", name="demo")
    await service.call(model)
```

## Features

- Async/await API
- TokenProvider supporting API keys and OAuth2
- ExampleService demonstrating unary RPC calls
- Pytest-based tests