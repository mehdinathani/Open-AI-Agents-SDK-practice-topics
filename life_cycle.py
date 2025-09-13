from agents import Runner
from geminiConfig import gemini_config
from my_agents import receiption_agent
import asyncio

async def main():
    result = await Runner.run(
        starting_agent=receiption_agent,
        input="i have a export shipment",
        run_config = gemini_config
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())