from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Mikkyydemo1", "Mikkyydemo1")

@mcp.tool("hello")
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

@mcp.resource("hello-{name}")
def get_greeting(name: str) -> str:
    """Returns a hello message."""
    return f"Hello, {name}!"
