from agents import Agent

import servers

FILE_SYSTEM_AGENT = None


async def initialize_file_system_agent():
    global FILE_SYSTEM_AGENT

    if servers.FILE_SYSTEM_SERVER is None:
        raise RuntimeError("FILE_SYSTEM_SERVER must be initialized first.")

    FILE_SYSTEM_AGENT = Agent(
        name="File system helper",
        handoff_description="Specialist agent for answering questions about files on a given file system.",
        instructions="Use the tools to read the filesystem and answer questions based on those files.",
        mcp_servers=[servers.FILE_SYSTEM_SERVER],
    )
