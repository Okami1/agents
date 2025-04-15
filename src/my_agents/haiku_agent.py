from agents import Agent


async def initialize_haiku_agent():
    print("  Initializing HAIKU_AGENT")

    return Agent(
        name="Haiku writer",
        handoff_description="Specialist agent for writing haikus",
        instructions="You write haikus based on user input. Return nothing but the haiku itself.",
    )
