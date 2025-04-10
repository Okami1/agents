from agents import Runner
import asyncio
from my_agents.orchestration_agent import orchestration_agent

async def main():
    result = await Runner.run(orchestration_agent, "who was the first president of the united states?")
    print(result.final_output)

    result = await Runner.run(orchestration_agent, "Write a haiku about pokemon")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())