from agents import Agent

HAIKU_AGENT = None


async def initialize_haiku_agent():
    print("  Haiku Agent")

    global HAIKU_AGENT

    HAIKU_AGENT = Agent(
        name="Haiku writer",
        handoff_description="Specialist agent for writing haikus",
        instructions="You write haikus based on user input. Return nothing but the haiku itself.",
    )
