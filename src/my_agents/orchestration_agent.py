from agents import Agent

import my_agents
import my_agents.brave_search_agent
import my_agents.weather_agent

ORCHESTRATION_AGENT = None


async def initialize_orchestration_agent():
    print("Initialization Orchestration Agent...")

    global ORCHESTRATION_AGENT

    if (
        my_agents.filesystem_agent.FILE_SYSTEM_AGENT is None
        or my_agents.haiku_agent.HAIKU_AGENT is None
        or my_agents.history_tutor_agent.HISTORY_TUTOR_AGENT is None
        or my_agents.weather_agent.WEATHER_AGENT is None
        or my_agents.brave_search_agent.BRAVE_SEARCH_AGENT is None
    ):
        raise RuntimeError(
            "Dependent agents are not initialized. Make sure all agents are initialized before orchestration."
        )

    ORCHESTRATION_AGENT = Agent(
        name="Triage Agent",
        instructions="You determine which agent to use based on the user's question. Don't try to answer the question yourself. Use the handoff agents to answer the question.",
        handoffs=[
            my_agents.haiku_agent.HAIKU_AGENT,
            my_agents.history_tutor_agent.HISTORY_TUTOR_AGENT,
            my_agents.filesystem_agent.FILE_SYSTEM_AGENT,
            my_agents.weather_agent.WEATHER_AGENT,
            my_agents.brave_search_agent.BRAVE_SEARCH_AGENT,
        ],
    )

    return ORCHESTRATION_AGENT
