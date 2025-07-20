from ast import arguments
import logging
from mcp import ClientSession, StdioServerParameters, types 
from mcp.client.stdio import stdio_client 

server_params = StdioServerParameters(
    command="mcp",
    args=["run", "server.py"],
    env=None,
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
          
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    
           # resources = await session.list_tools()
            # for resource in resources:
            #     print(f"Tools:", resource)

            result = await session.call_tool("hello",arguments={"a": 13, "b": 17 })
            print(result.content)

            # content = await session.get_resource("hello-Mikkyy")
            # print(f"Greeting: {content.content}")
            
            # print("Session closed.")

            
if __name__ == "__main__":
    import asyncio
    asyncio.run(run())