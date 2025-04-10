from agents import Agent

haiku_agent = Agent(
    name="Haiku writer",
    handoff_description="Specialist agent for writing haikus",
    instructions="You write haikus based on user input. Return nothing but the haiku itself.",
)