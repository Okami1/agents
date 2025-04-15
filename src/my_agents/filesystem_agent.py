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
        instructions="Use the tools regarding the file system to execute user requests."
        "Make sure to do broad searches on file and their contents if the user doesn't provide specific file names.",
        mcp_servers=[file_system_server],
    )
