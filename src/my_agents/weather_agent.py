from agents import Agent

import servers

WEATHER_AGENT = None


async def initialize_weather_agent():
    print("  Weather Agent")

    global WEATHER_AGENT

    weather_server = servers.SERVERS.get("WEATHER_SERVER")

    if weather_server is None:
        raise RuntimeError("WEATHER_SERVER must be initialized first.")

    WEATHER_AGENT = Agent(
        name="weather helper",
        handoff_description="Specialist agent for answering questions about including alerts and air quality.",
        instructions="Use the tools to answer questions about the weather.",
        mcp_servers=[weather_server],
    )
