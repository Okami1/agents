from agents import Agent

from .filesystem_agent import FILE_SYSTEM_AGENT
from .haiku_agent import HAIKU_AGENT
from .history_tutor_agent import HISTORY_TUTOR_AGENT

ORCHESTRATION_AGENT = None


async def initialize_orchestration_agent():
    global ORCHESTRATION_AGENT

    if FILE_SYSTEM_AGENT is None or HAIKU_AGENT is None or HISTORY_TUTOR_AGENT is None:
        raise RuntimeError(
            "Dependent agents are not initialized. Make sure all agents are initialized before orchestration."
        )

    ORCHESTRATION_AGENT = Agent(
        name="Triage Agent",
        instructions="You determine which agent to use based on the user's question",
        handoffs=[
            HAIKU_AGENT,
            HISTORY_TUTOR_AGENT,
            FILE_SYSTEM_AGENT,
        ],
    )
