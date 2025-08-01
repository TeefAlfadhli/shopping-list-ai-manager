# NOT PRODUCTION REQUIRED
#TODO: Ignore this file when production ready -- this is just for testing
import uuid
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            # You can now interact with the server using the session object
            # List all tools exposed by the server
            tools_list = await session.list_tools()

# For each tool, display its name, description, and input schema
            for tool in tools_list.tools:
                print(f"Name: {tool.name}")
                print(f"Description: {tool.description}")
                print(f"Input Schema:\n{tool.inputSchema}\n")

            # Add a new item to the shopping list
            response_add = await session.call_tool("add_item",{"name": "Bananas","quantity": 3})

            # Extract and print the ID of the newly added item
            added_id = response_add.content[0].text
            print(f"Added item ID: {added_id}")
            
            # Retrieve all shopping list items
            response_fetch = await session.call_tool("fetch_items", {})

            # Print each item in the shopping list
            print("Current shopping list items:")
            for item in response_fetch.content:
                print(item.text)
            



if __name__ == "__main__":
    asyncio.run(main())