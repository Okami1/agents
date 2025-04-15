import asyncio
import os

from agents.mcp import MCPServer, MCPServerStdio

SERVERS: dict[str, MCPServer] = {}
LIST_SERVERS: list[MCPServer] = []


async def start_servers() -> list[MCPServer]:
    print("Starting servers...")
    global SERVERS

    current_dir = os.path.dirname(os.path.abspath(__file__))

    ## File system server
    file_samples_dir = os.path.join(current_dir, "sample_files")

    print(
        f"  Filesystem Server using npx: @modelcontextprotocol/server-filesystem with {file_samples_dir}"
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
    LIST_SERVERS.append(file_system_server)

    ## Brave search server
    print("  Brave Search Server using npx: @modelcontextprotocol/server-brave-search")

    brave_search_server = MCPServerStdio(
        name="Brave Search Server, via npx",
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search"],
            "env": {
                "BRAVE_API_KEY": os.environ.get("BRAVE_API_KEY", None),
            },
        },
    )
    await brave_search_server.connect()

    SERVERS["BRAVE_SEARCH_SERVER"] = brave_search_server
    LIST_SERVERS.append(brave_search_server)

    ## Weather service server
    service_path = os.path.join(
        current_dir, "my_servers", "Weather-MCP-ClaudeDesktop", "main.py"
    )

    print(f"  Weather Server using local python: {service_path}")

    weather_server = MCPServerStdio(
        name="Weather Server, via python",
        params={
            "command": "python",
            "args": [service_path],
        },
    )
    await weather_server.connect()

    SERVERS["WEATHER_SERVER"] = weather_server
    LIST_SERVERS.append(weather_server)


async def cleanup_servers() -> None:
    # Cleanup the servers in reverse initialization order
    for server in reversed(LIST_SERVERS):
        await server.cleanup()
        await asyncio.sleep(1)
