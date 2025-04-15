from agents import Agent
from agents.mcp import MCPServer


async def initialize_file_system_agent(file_system_server: MCPServer):
    print("  Initializing FILE_SYSTEM_AGENT")

    if file_system_server is None:
        raise RuntimeError(
            "The FILE_SYSTEM_SERVER must be initialized before the File System Agent can be initialized."
        )

    return Agent(
        name="File system helper",
        handoff_description="Specialist agent for answering questions about files on a given file system.",
        instructions="Use the tools to read the filesystem and answer questions based on those files.",
        mcp_servers=[file_system_server],
    )
