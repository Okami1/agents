from agents import Agent
from agents.mcp import MCPServer


async def initialize_math_agent(wolfram_alpha_server: MCPServer):
    print("  Initializing WOLFRAM_ALPHA_SERVER")

    if wolfram_alpha_server is None:
        raise RuntimeError("WOLFRAM_ALPHA_SERVER must be initialized first.")

    return Agent(
        name="math helper",
        handoff_description="Specialist agent for answering questions mathematics.",
        instructions="Answer queries to the best of your abilities, use the tools if necessary.",
        mcp_servers=[wolfram_alpha_server],
    )
