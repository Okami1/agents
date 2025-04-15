import asyncio

from agents import Runner

from my_agents import AgentsClient
from servers import ServersClient


async def main(request: str):
    servers_client = ServersClient()
    servers = await servers_client.start_servers()

    agents_client = AgentsClient()
    await agents_client.initialize_agents(servers=servers)
    orchestration_agent = await agents_client.initialize_orchestration_agent(
        use_initialized_agents=True
    )

    print("Processing request...")
    result = await Runner.run(
        orchestration_agent,
        request,
    )
    print(result.final_output)

    await servers_client.cleanup_servers()


if __name__ == "__main__":
    asyncio.run(main("What is the goal of the game Twilight Imperium?"))
    # asyncio.run(main("What is the weather like in Copenhagen?"))
    # asyncio.run(main("read the files and list them"))
    # asyncio.run(main("who was the first president of the united states?"))
    # asyncio.run(main("Write a haiku about pokemon"))
