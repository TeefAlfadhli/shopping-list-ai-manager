import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

# Load environment variables from .env file
load_dotenv()

async def main():
    server_params = {
        "command": "python",
        "args": ["mcp_server.py"]
    }

    async with MCPServerStdio(params=server_params) as mcp_server:
        # Create the agent and provide the MCP server
        agent = Agent(
            name="Shopping Assistant",
            instructions="You are an assistant that uses shopping list tools to help manage a shopping list.",
            model="gpt-4.1",
            mcp_servers=[mcp_server]  # List of MCP servers available
        )

        # Run the agent with a query
        result = await Runner.run(agent, "view the updatedshopping list")
        
        # Print the final output
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())