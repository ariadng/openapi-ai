# OpenAPI AI

This is a Python library that helps AI agents to connect to, talk to, and consume existing web REST API endpoints built with [OpenAPI standard](https://www.openapis.org/). It does so by generating tools at runtime that can be called by LLM-based agents that built with [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) or [Google ADK](https://google.github.io/adk-docs/).

![OpenAPI AI](https://yvkbpmmzjmfqjxusmyop.supabase.co/storage/v1/object/public/github//openapi_ai.png)

## Project Checklist

- ✅ Generate python functions from OpenAPI server endpoints
- Generate function tools for OpenAPI Agent SDK
- Generate function tools for Google ADK
- Integrate Pydantic
- Support for endpoints with multiple path parameters
- Authentication

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
