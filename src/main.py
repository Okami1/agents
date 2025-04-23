import asyncio

from agents import Runner, RunResult

from my_agents import AgentsClient
from servers import ServersClient


def update_history(response: RunResult, messages_to_keep: int = 10) -> list[dict]:
    history = response.to_input_list()
    history = [msg for msg in history if msg.get("role") and msg.get("content")]
    return history[-messages_to_keep:]


async def main():
    servers_client = ServersClient()
    servers = await servers_client.start_servers()

    agents_client = AgentsClient()
    await agents_client.initialize_agents(servers=servers)
    orchestration_agent = await agents_client.initialize_orchestration_agent(
        use_initialized_agents=True,
    )

    print("Client ready!")
    history = []
    while True:
        try:
            query = input("\nQuery: ").strip()

            if query.lower() == "quit":
                break

            response = await Runner.run(
                starting_agent=orchestration_agent,
                input=history + [{"role": "user", "content": query}],
                context=history,
            )

            history = update_history(response)

            print("\n" + response.final_output)

        except Exception as e:
            print(f"\nError: {str(e)}")

    await servers_client.cleanup_servers()


if __name__ == "__main__":
    asyncio.run(main())
    # "What is the goal of the game Twilight Imperium?"
    # "What is the weather like in Copenhagen?"
    # "What are my favorite songs?"
    # "Find x in this equation: x^3 - 4x^2 + 6x - 24 = 0"
    # "who was the first president of the united states?"
    # "Write a haiku about pokemon"
