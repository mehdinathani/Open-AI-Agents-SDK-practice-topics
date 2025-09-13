import os
from agents import Agent, Runner, set_trace_processors, set_tracing_export_api_key, trace,RunConfig
from agents.tracing.processors import default_processor
from dotenv import load_dotenv
from geminiConfig import gemini_config,model

load_dotenv()
set_trace_processors([default_processor()])
api_key = os.getenv("OPENAI_API_KEY")
set_tracing_export_api_key(api_key)

agent = Agent(
    name="SimpleAgent",
    instructions="You are a helpful assistant.",
    model=model
)

async def main():
    with trace("Workflow"):
        result = await Runner.run(
            starting_agent=agent,
            input="What is agentic AI",
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())