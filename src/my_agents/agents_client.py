from agents import Agent
from agents.mcp import MCPServer

from .brave_search_agent import initialize_brave_search_agent
from .filesystem_agent import initialize_file_system_agent
from .haiku_agent import initialize_haiku_agent
from .history_tutor_agent import initialize_history_tutor_agent
from .math_agent import initialize_math_agent
from .weather_agent import initialize_weather_agent


class AgentsClient:
    def __init__(self):
        self.orchestration_agent = None
        self.agents: dict[str, Agent] = {}

    async def initialize_agents(self, servers: dict[str, MCPServer]):
        # TODO: Expand this with information about specifically which initialization failed
        print("Initializing agents...")

        self.agents["FILE_SYSTEM_AGENT"] = await initialize_file_system_agent(
            file_system_server=servers.get("FILE_SYSTEM_SERVER"),
            sequential_thinking_server=servers.get("SEQUENTIAL_THINKING_SERVER"),
        )
        self.agents["HAIKU_AGENT"] = await initialize_haiku_agent()
        self.agents["HISTORY_TUTOR_AGENT"] = await initialize_history_tutor_agent()
        self.agents["WEATHER_AGENT"] = await initialize_weather_agent(
            weather_server=servers.get("WEATHER_SERVER")
        )
        self.agents["BRAVE_SEARCH_AGENT"] = await initialize_brave_search_agent(
            brave_search_server=servers.get("BRAVE_SEARCH_SERVER")
        )
        self.agents["MATH_AGENT"] = await initialize_math_agent(
            wolfram_alpha_server=servers.get("WOLFRAM_ALPHA_SERVER")
        )

        return self.agents

    async def initialize_orchestration_agent(
        self,
        use_initialized_agents: bool = True,
    ):
        print("Initializating Orchestration Agent...")

        if use_initialized_agents:
            handoff_agents = [agent for agent in self.agents.values()]
        else:
            handoff_agents = []

        self.orchestration_agent = Agent(
            name="Triage Agent",
            instructions="You determine which agent to use based on the user's question. "
            "Don't try to answer the question yourself, instead use the handoff agents to answer the question. ",
            handoffs=handoff_agents,
        )

        return self.orchestration_agent

    async def populate_orchestration_agents(self, handoff_agents: list[Agent]):
        self.orchestration_agent.handoffs += handoff_agents
        return self.orchestration_agent

    async def remove_orchestration_agents(self, agents_to_remove: list[str]):
        self.orchestration_agent.handoffs = [
            agent
            for agent in self.orchestration_agent.handoffs
            if agent.agent_name not in agents_to_remove
        ]
        return self.orchestration_agent
