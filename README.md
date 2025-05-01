# OpenAPI AI

This is a Python library that helps AI agents to connect to, talk to, and consume existing web REST API endpoints built with [OpenAPI standard](https://www.openapis.org/). It does so by generating tools at runtime that can be called by LLM-based agents built with [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) or [Google ADK](https://google.github.io/adk-docs/).

![OpenAPI AI](https://yvkbpmmzjmfqjxusmyop.supabase.co/storage/v1/object/public/github//openapi_ai.png)

## Use Cases

### 1. Enterprise Automation & Internal Tools Integration

Many companies have internal web tools for things like HR, project tracking, or customer information. Often, these tools have APIs described using the OpenAPI standard. **OpenAPI AI** library can read these descriptions and automatically create Python functions. This allows an AI agent (built with OpenAI or Google agent SDKs) to use these functions to interact with the company's tools, potentially letting users ask for information or perform simple tasks in one place.

### 2. Giving AI Agents Access to Live Information

AI models know a lot, but they don't always have the latest information like current weather, live stock prices, or if a product is in stock right now. If a service provides this live data through an API with an OpenAPI description, **OpenAPI AI** library can generate tools for it. An AI agent can then use these tools to fetch the real-time data when needed, helping it give more current and specific answers.

### 3. Helping AI Agents Interact with External Web Services

Sometimes you might want an AI agent to do something on another website or platform, like adding an issue to GitHub or posting a basic message. If these external services offer an API documented with OpenAPI, **OpenAPI AI** library can create the functions for those actions. An agent using these functions (with the right permissions and authentication) could then perform tasks on those platforms based on user requests.

### 4. Speeding Up AI Agent Development with API Integration

Certain tasks involve multiple steps using different APIs, for example, checking flight availability and then looking for hotels, or getting data from a CRM and sending it to a marketing tool. If the APIs for these steps are described using OpenAPI, **OpenAPI AI** library can generate functions for each one. An AI agent could then potentially manage the sequence of calling these functions to complete the overall task.

### 5. Rapid Prototyping and Development

When building an AI agent that needs to use web APIs, developers typically write code to make the API calls. **OpenAPI AI** library helps automate part of this. By reading an API's OpenAPI specification file, it generates the basic Python functions an agent (using OpenAI or Google SDKs) needs to call that API. This can save development time, letting builders focus more on the agent's core logic rather than writing repetitive API connection code.

### 6. Enabling AI for Legacy Systems

Sometimes, older company systems don't have modern APIs that AI agents can easily use. A common approach is to build a simpler, modern API "wrapper" around the old system and describe this wrapper using OpenAPI. **OpenAPI AI** library can then read the wrapper's OpenAPI description and generate functions for it, providing a way for an AI agent to communicate with the underlying legacy system indirectly.

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
