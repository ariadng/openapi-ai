# OpenAPI AI Agent Tools Generator

Generate function tools from OpenAPI server that can be used with LLM AI agents at runtime.

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
