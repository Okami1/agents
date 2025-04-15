from agents import Agent

import servers

BRAVE_SEARCH_AGENT = None


async def initialize_brave_search_agent():
    global BRAVE_SEARCH_AGENT

    brave_search_server = servers.SERVERS.get("BRAVE_SEARCH_SERVER")
    if brave_search_server is None:
        raise RuntimeError("BRAVE_SEARCH_SERVER must be initialized first.")

    BRAVE_SEARCH_AGENT = Agent(
        name="Brave search helper",
        handoff_description="Specialist agent for searching the web or locally using the Brave API.",
        instructions="Use the tools to search to find results that callow you to answer the user queries.",
        mcp_servers=[brave_search_server],
    )
