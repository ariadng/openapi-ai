import os
from dotenv import load_dotenv
from agents import Agent, Runner
from openapi_ai import OpenAPITools

load_dotenv()

async def main():
    openapi_tools = OpenAPITools(os.getenv("API_URL"), remove_prefix=os.getenv("API_PREFIX"))

    agent = Agent(
        name="Haiku trading agent",
        instructions="You are a trading assistant. Always answer in haiku form.",
        model="gpt-4o",
        tools=openapi_tools.get_openai_tools(),
    )

    result = await Runner.run(agent, "What is my current account info?")
    print(result.final_output)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
