import asyncio
import os

from agents.mcp import MCPServer, MCPServerStdio


class ServersClient:
    def __init__(self):
        self.servers: dict[str, MCPServer] = {}
        self.server_list: list[MCPServer] = []

        self.current_dir = os.path.dirname(os.path.abspath(__file__))

    async def start_servers(self) -> dict[str, MCPServer]:
        print("Starting servers...")

        ## File system server
        file_samples_dir = os.path.join(self.current_dir, "sample_files")

        print(
            f"  Filesystem Server using npx: @modelcontextprotocol/server-filesystem with {file_samples_dir}"
        )

        file_system_server = MCPServerStdio(
            name="Filesystem Server, via npx",
            params={
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    file_samples_dir,
                ],
            },
        )
        await file_system_server.connect()

        self.servers["FILE_SYSTEM_SERVER"] = file_system_server
        self.server_list.append(file_system_server)

        ## Brave search server
        print(
            "  Brave Search Server using npx: @modelcontextprotocol/server-brave-search"
        )

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

        self.servers["BRAVE_SEARCH_SERVER"] = brave_search_server
        self.server_list.append(brave_search_server)

        ## Weather service server
        service_path = os.path.join(
            self.current_dir, "my_servers", "Weather-MCP-ClaudeDesktop", "main.py"
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

        self.servers["WEATHER_SERVER"] = weather_server
        self.server_list.append(weather_server)

        ## Wolfram Alpha server
        service_path = os.path.join(
            self.current_dir, "my_servers", "wolframalpha_server", "main.py"
        )

        print(f"  Wolfram Alpha Server using local python: {service_path}")

        wolfram_alpha_server = MCPServerStdio(
            name="Wolfram Alpha Server, via python",
            params={
                "command": "python",
                "args": [service_path],
            },
        )
        await wolfram_alpha_server.connect()

        self.servers["WOLFRAM_ALPHA_SERVER"] = wolfram_alpha_server
        self.server_list.append(wolfram_alpha_server)

        ## Sequential thinking server
        print(
            "  Sequential Thinking Server using npx @modelcontextprotocol/server-sequential-thinking"
        )

        sequential_thinking_server = MCPServerStdio(
            name="Sequential Thinking Server, via npx",
            params={
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
            },
        )
        await sequential_thinking_server.connect()

        self.servers["SEQUENTIAL_THINKING_SERVER"] = sequential_thinking_server
        self.server_list.append(sequential_thinking_server)

        return self.servers

    async def cleanup_servers(self) -> None:
        print("Cleaning up servers...")
        # Cleanup the servers in reverse initialization order
        for server in reversed(self.server_list):
            await server.cleanup()
            await asyncio.sleep(1)
