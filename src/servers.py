import os
from typing import Union

from agents.mcp import (
    MCPServerSse,
    MCPServerStdio,
)

FILE_SYSTEM_SERVER = None


async def start_servers() -> list[Union[MCPServerStdio, MCPServerSse]]:
    global FILE_SYSTEM_SERVER

    current_dir = os.path.dirname(os.path.abspath(__file__))
    samples_dir = os.path.join(current_dir, "sample_files")
    file_system_server = MCPServerStdio(
        name="Filesystem Server, via npx",
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", samples_dir],
        },
    )

    FILE_SYSTEM_SERVER = file_system_server
