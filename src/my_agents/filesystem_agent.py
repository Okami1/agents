from agents import Agent
from agents.mcp import MCPServer


async def initialize_file_system_agent(
    file_system_server: MCPServer, sequential_thinking_server: MCPServer
) -> Agent:
    print("  Initializing FILE_SYSTEM_AGENT")

    if file_system_server is None:
        raise RuntimeError(
            "The FILE_SYSTEM_SERVER must be initialized before the File System Agent can be initialized."
        )

    if sequential_thinking_server is None:
        raise RuntimeError(
            "The SEQUENTIAL_THINKING_SERVER must be initialized before the File System Agent can be initialized."
        )

    return Agent(
        name="File system helper",
        handoff_description="Specialist agent for answering questions about files on a given file system.",
        instructions="Help users by performing the requested action using the tools to access the file system. "
        "Use the sequential thinking tool to plan out the steps needed to complete the task. "
        "Remember that the exact file names may not be provided.",
        mcp_servers=[file_system_server, sequential_thinking_server],
    )
