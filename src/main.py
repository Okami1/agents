import asyncio

from agents import Runner

import servers
from my_agents import initialize_agents
from my_agents.orchestration_agent import (
    initialize_orchestration_agent,
)


async def main(request: str):
    await servers.start_servers()
    await initialize_agents()
    orchestration_agent = await initialize_orchestration_agent()

    result = await Runner.run(
        orchestration_agent,
        request,
    )
    print(result.final_output)

    await servers.cleanup_servers()


if __name__ == "__main__":
    asyncio.run(main("Why do asian pandas have trouble breeding in captivity?"))
    # asyncio.run(main("What is the weather like in Copenhagen?"))
    # asyncio.run(main("read the files and list them"))
    # asyncio.run(main("who was the first president of the united states?"))
    # asyncio.run(main("Write a haiku about pokemon"))
