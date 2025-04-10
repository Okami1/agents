import asyncio

from agents import Runner

import my_agents
import servers


async def main(request: str):
    await servers.start_servers()
    await my_agents.initialize_agents()

    result = await Runner.run(
        my_agents.ORCHESTRATION_AGENT,
        request,
    )
    print(result.final_output)


if __name__ == "__main__":
    # asyncio.run(main("read the files and list them"))
    asyncio.run(main("who was the first president of the united states?"))
    # asyncio.run(main("Write a haiku about pokemon"))
