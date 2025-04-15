from agents import Agent
from agents.mcp import MCPServer


async def initialize_brave_search_agent(brave_search_server: MCPServer):
    print("  Initializing BRAVE_SEARCH_AGENT")

    if brave_search_server is None:
        raise RuntimeError("BRAVE_SEARCH_SERVER must be initialized first.")

    return Agent(
        name="Brave search helper",
        handoff_description="Specialist agent for searching the web or locally using the Brave API.",
        instructions="Use the tools to search to find results that callow you to answer the user queries.",
        mcp_servers=[brave_search_server],
    )
