import json
from mcp.server.fastmcp import FastMCP
from .scanner import scan_target

mcp = FastMCP("skillspector")

@mcp.tool()
def scan_skill(target: str) -> str:
    """
    Scan an AI agent skill repository or directory for security vulnerabilities.
    
    Args:
        target: URL (e.g., https://github.com/someone/skill) or local path.
    """
    result = scan_target(target)
    return json.dumps(result, indent=2)

def run_mcp_server():
    mcp.run()
