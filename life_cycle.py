from agents import Runner, trace
from geminiConfig import gemini_config
from my_agents import reception_agent
import asyncio
from run_lifecycle import myrunhooks

async def main():
    history = []
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat.")
            break
        if not user_input:
            print("Please enter a message.")
            continue
        history.append({"role":"user", "content":user_input})
        result = await Runner.run(
            starting_agent=reception_agent,
            input=history,
            run_config = gemini_config,
            hooks=myrunhooks()
        )
        if result.final_output:
            history.append({"role":"assistant", "content":result.final_output})
            print(f"Assistant : {result.final_output}")  

if __name__ == "__main__":
    asyncio.run(main())