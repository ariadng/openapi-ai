# OpenAPI Agent Tools

Generate function tools from OpenAPI server that can be used with LLM AI agents.

## Project Roadmap

- ✅ Generate python functions from OpenAPI server endpoints
- Generate function tools for OpenAPI Agent SDK
- Generate function tools for Google ADK

## Installation

```bash
pip install openapi-agent-tools
```

## Usage

```python
from openapi_agent_tools import generate_tools

spec = load_spec('https://api.example.com/openapi.json')

generate_tools(spec)
```

## License

MIT
