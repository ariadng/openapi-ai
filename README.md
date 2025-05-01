# OpenAPI AI Agent Tools Generator

Helps your AI agents to connect to, talk to, and consume existing web REST API endpoints built with [OpenAPI standard](https://www.openapis.org/).

![OpenAPI AI](https://yvkbpmmzjmfqjxusmyop.supabase.co/storage/v1/object/public/github//openapi_ai.png)

## Project Checklist

- ✅ Generate python functions from OpenAPI server endpoints
- Generate function tools for OpenAPI Agent SDK
- Generate function tools for Google ADK
- Integrate pydantic for better typings
- Support for endpoints with multiple path parameters

## Installation

```bash
pip install openapi-ai
```

## Usage

```python
from openapi_ai import generate_tools

spec = load_spec('https://api.example.com/openapi.json')

generate_tools(spec)
```

## License

MIT
