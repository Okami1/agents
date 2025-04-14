import asyncio
import os

from agents.mcp import MCPServer, MCPServerStdio

SERVERS: dict[str, MCPServer] = {
    "FILE_SYSTEM_SERVER": None,
    "WEATHER_SERVER": None,
}


async def start_servers() -> list[MCPServer]:
    global SERVERS

    current_dir = os.path.dirname(os.path.abspath(__file__))

    ## File system server
    file_samples_dir = os.path.join(current_dir, "sample_files")

    print(
        f"Creating filesystem server using npx @ @modelcontextprotocol/server-filesystem with: {file_samples_dir}"
    )

    file_system_server = MCPServerStdio(
        name="Filesystem Server, via npx",
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", file_samples_dir],
        },
    )
    await file_system_server.connect()

    SERVERS["FILE_SYSTEM_SERVER"] = file_system_server

    ## Weather service server
    service_path = os.path.join(
        current_dir, "my_servers", "Weather-MCP-ClaudeDesktop", "main.py"
    )

    print(f"Creating weather server using python @ {service_path}")

    weather_server = MCPServerStdio(
        name="Weather Server, via python",
        params={
            "command": "python",
            "args": [service_path],
        },
    )
    await weather_server.connect()

    SERVERS["WEATHER_SERVER"] = weather_server


async def cleanup_servers() -> None:
    cleanup_tasks = []
    for server in SERVERS.values():
        cleanup_tasks.append(asyncio.create_task(server.cleanup()))

    if cleanup_tasks:
        try:
            await asyncio.gather(*cleanup_tasks, return_exceptions=True)
        except Exception as e:
            print(f"Warning during final cleanup: {e}")
