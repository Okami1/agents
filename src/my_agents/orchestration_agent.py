from agents import Agent
from my_agents.haiku_agent import haiku_agent

orchestration_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[haiku_agent],
)