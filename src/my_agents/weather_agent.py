from agents import Agent
from agents.mcp import MCPServer


async def initialize_weather_agent(weather_server: MCPServer):
    print("  Initializing WEATHER_AGENT")

    if weather_server is None:
        raise RuntimeError("WEATHER_SERVER must be initialized first.")

    return Agent(
        name="weather helper",
        handoff_description="Specialist agent for answering questions about weather including alerts and air quality.",
        instructions="Use the tools to answer questions about the weather.",
        mcp_servers=[weather_server],
    )
