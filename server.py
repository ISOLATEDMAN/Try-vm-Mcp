from mcp.server import FastMCP

mcp = FastMCP("YOO")

@mcp.tool()
def greeting():
    return "welcome to the mcp"



if __name__ == "__main__":
    mcp.run("streamable-http")